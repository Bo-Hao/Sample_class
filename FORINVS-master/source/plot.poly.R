plot.poly<-function(data,area,px,py,pr,pphi,ptheta,pbound){
         ### Generate a list of sample trees from a plot of any polygon shape 
         ###    data: dataset [spatstat object]
         ###    area: enclosed area of the dataset [spatstat object]
         ###    px: x-coordinate of plot center [meter]
         ###    py: y-coordinate of plot center [meter]
         ###    pr: radial coordinate in Polar Coordinate System arranged in counter-clockwise with East at 0 degree [vector; meter]
         ###    pphi: angular coordinate in Polar Coordinate System arranged in counter-clockwise with East at 0 degree [vector; radian]
         ###    ptheta: rotation angle of polygon in Polar Coordinate System in counter-clockwise with East at 0 degree [radian]
         ###    pbound: plot boundary overlap correction method
         ### Output: treelist [data frame]

          ## Find Cartesian coordinate of the vertices of the polygon 
           # Extract xy-coordinates of vertices by complex number and Polar Coordinates
             z<-complex(arg=pphi+ptheta,mod=pr)
             vertex<-cbind(Re(z)+px,Im(z)+py) 
 
          ## Generate spatstat object for polygon plot
             win<-owin(poly=vertex)

          ## Extract sample trees
             treelist<-data[win]
             treelist<-treelist$marks

          ## Compile plot treelist
             if(nrow(treelist)==0){
                 # Empty treelist
                   treelist<-data.frame(treelist,"TF"=numeric())   
             }else{
                 # Non-empty treelist
                 # Plot boundary overlap correction 
                   treelist.dbl<-pbdry(area,treelist,px,py,pbound)
                   treelist<-rbind(treelist,treelist.dbl)

                 # Calculate Tree Factor (TF) for individual tree
                   treelist$TF<-10000/area.owin(win)
             }   

   return(treelist)
}
