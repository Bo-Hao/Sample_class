plot.hps<-function(data,area,px,py,pbaf,pbound){
         ### Generate a list of sample trees from Horizontal Point Sampling 
         ###    data: dataset [spatstat object]
         ###    area: enclosed area of the dataset [spatstat object]
         ###    px: x-coordinate of plot center [meter]
         ###    py: y-coordinate of plot center [meter]
         ###    pbaf: plot Basal Area Factor [m^2/ha]
         ###    pbound: plot boundary overlap correction method
         ### Output: treelist [data frame]

          ## Extract potential sample trees based on maximum limiting distance
             LDmax<-max(data$marks$dbh)/(2*sqrt(pbaf))*1.1
             win<-disc(radius=LDmax,centre=c(px,py),npoly=10000)
             tree<-data[win]$marks

          ## Extract sample trees
           # Calculate tree distance to plot center
             tdist<-sqrt((px-tree$x)^2+(py-tree$y)^2)

           # Calculate limiting distance
             LD<-tree$dbh/(2*sqrt(pbaf))

           # Sample trees are those with tdist<=LD
             treelist<-tree[tdist<=LD,]
 
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
                   treelist$TF<-pbaf/(pi/40000*treelist$dbh^2)
             }

   return(treelist)
}
