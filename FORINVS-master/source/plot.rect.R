plot.rect<-function(data,area,px,py,pl,pw,ptheta,pbound){
         ### Generate a list of sample trees from a square or rectangular plot
         ###    data: dataset [spatstat object]
         ###    area: enclosed area of the dataset [spatstat object]
         ###    px: x-coordinate of plot center [meter]
         ###    py: y-coordinate of plot center [meter]
         ###    pl: length or long side of the rectangular plot [meter]
         ###    pw: width or short side of the rectangular plot [meter]
         ###    ptheta: rotation angle of long side of the rectangular plot in Polar Coordinate System [counter-clockwise with East at 0 rad; radian]
         ###    pbound: plot boundary overlap correction method
         ### Output: treelist [data frame]

          ## Find angular (phi) and radial (r) coordinates of four vertices in a counter-clockwise manner in Polar Coordinate System
          ## Order of vertices are UpperRight, UpperLeft, LowerLeft, and LowerRight
             phi<-c(atan(pw/pl),pi-atan(pw/pl),pi+atan(pw/pl),2*pi-atan(pw/pl))+ptheta
             r<-rep(sqrt((pl^2+pw^2))/2,4)

           # Extract Cartesian coordinates of vertices
             z<-complex(arg=phi,mod=r)
             vertex<-cbind(Re(z)+px,Im(z)+py) 
 
         ## Generate spatstat object for rectangular plot
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
                   treelist$TF<-10000/(pl*pw)
             }   

   return(treelist)
}
