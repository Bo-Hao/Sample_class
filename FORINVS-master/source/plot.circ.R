plot.circ<-function(data,area,px,py,pr,pbound){
         ### Generate a list of sample trees from a circular plot
         ###    data: dataset [spatstat object]
         ###    area: enclosed area of the dataset [spatstat object]
         ###    px: x-coordinate of plot center [meter]
         ###    py: y-coordinate of plot center [meter]
         ###    pr: plot radius [meter]
         ###    pbound: plot boundary overlap correction method
         ### Output: treelist [data frame]

          ## Generate circular plot window
             win<-disc(radius=pr,centre=c(px,py),npoly=10000)

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
                   treelist$TF<-10000/(pi*pr^2)
             }

   return(treelist)
}

