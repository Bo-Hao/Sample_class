plot.clus<-function(data,area,cx,cy,cr,cphi,ctheta,cbound,ptype,pdimn,pbound){
         ### Generate a list of sample trees from a cluster plot
         ###    data: dataset [spatstat object]
         ###    area: enclosed area of the dataset [spatstat object]
         ###    cx: x-coordinate of cluster center [meter]
         ###    cy: y-coordinate of cluster center [meter]
         ###    cr: subplot center in radial coordinate in Polar Coordinate System arranged in counter-clockwise with East at 0 degree [vector; meter]
         ###    cphi: subplot center in angular coordinate in Polar Coordinate System arranged in counter-clockwise with East at 0 degree [vector; radian]   
         ###    ctheta: rotation angle of cluster plot in Polar Coordinate System in counter-clockwise with East at 0 degree [radian]
         ###    cbound: boundary overlap correction method for cluster 
         ###    ptype: subplot type
         ###    pdimn: subplot dimension corresponding to subplot type [unit depends on subplot type]
         ###    pbound: boundary overlap correction method for subplot
         ### Output: treelist [data frame]

          ## Find Cartesian xy-coordinates of subplot centers
             cz<-complex(arg=cphi+ctheta,mod=cr)
             cvertex<-cbind(Re(cz)+cx,Im(cz)+cy)

          ## Cluster boundary overlap correction   
             cvertex.cor<-cbdry(area,cx,cy,cvertex,cbound)

          ## Extract sample trees
             treelist<-switch(ptype,
                              "circ"=lapply(1:nrow(cvertex.cor),function(i) data.frame(subplot=i,plot.circ(data,area,cvertex.cor[i,1],cvertex.cor[i,2],pdimn,pbound))),
                              "hps"=lapply(1:nrow(cvertex.cor),function(i) data.frame(subplot=i,plot.hps(data,area,cvertex.cor[i,1],cvertex.cor[i,2],pdimn,pbound))),
                              "poly"=lapply(1:nrow(cvertex.cor),function(i) data.frame(subplot=i,plot.poly(data,area,cvertex.cor[i,1],cvertex.cor[i,2],pdimn[,1],pdimn[,2],pdimn[,3],pbound))),
                              "rect"=lapply(1:nrow(cvertex.cor),function(i) data.frame(subplot=i,plot.rect(data,area,cvertex.cor[i,1],cvertex.cor[i,2],pdimn[1],pdimn[2],pdimn[3],pbound)))                      
                              )
             treelist<-do.call(rbind,treelist)

   return(treelist)
}
