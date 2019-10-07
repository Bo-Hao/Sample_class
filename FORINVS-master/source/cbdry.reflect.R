cbdry.reflect<-function(area,cx,cy,cvertex){
         ### Reflection method for subplot centers of a cluster plot falling outside study area (Valentine et al. 2006)
         ###    area: enclosed area of the dataset [spatstat object]
         ###    cx: x-coordinate of cluster center [meter]
         ###    cy: y-coordinate of cluster center [meter]
         ###    cvertex: Cartesian xy-coordinates of subplot centers [meter]

          ## Internal functions
             intersect.segment<-function(seg1,seg2){
                      ### "Intersection point of two line segments in 2 dimensions" by Paul Bourke (1989) 
                      ### http://paulbourke.net/geometry/pointlineplane/   

                       ## Define parameters
                          x1<-seg1[1,1];y1<-seg1[1,2]
                          x2<-seg1[2,1];y2<-seg1[2,2]
                          x3<-seg2[1,1];y3<-seg2[1,2]
                          x4<-seg2[2,1];y4<-seg2[2,2]
                        
                       ## Numerators and denominator
                          denom<-(y4-y3)*(x2-x1)-(x4-x3)*(y2-y1)
                          numea<-(x4-x3)*(y1-y3)-(y4-y3)*(x1-x3)
                          numeb<-(x2-x1)*(y1-y3)-(y2-y1)*(x1-x3)   
                       
                       ## Determine intersection point
                          ua<-numea/denom
                          ub<-numeb/denom
                          if(ua>=0 && ua<=1 && ub>=0 && ub<=1){
                               x<-x1+ua*(x2-x1)
                               y<-y1+ua*(y2-y1)
                          }else{
                               x<-NULL
                               y<-NULL
                          }

                       ## Output intersection point
                          out<-c(x,y)

                 return(out)             
             }

             reflect<-function(avertex,cx,cy,cvertex.out){
                      ### Reflect subplot centers that are outside the study area into the study area
                       
                       ## Declare output
                          rfl<-NULL

                       ## Reflect each subplot center
                          for(i in 1:nrow(cvertex.out)){
                               # Declare output
                                 intersect.pt<-NULL

                               # Line segment 1: from subplot center to cluster center  
                                 seg1<-rbind(cvertex.out[i,],c(cx,cy))
               
                               # Line segment 2: each boundary line of study area
                                 for(j in 1:(nrow(avertex)-1)){
                                      seg2<-avertex[j:(j+1),]
                                      tmp<-intersect.segment(seg1,seg2)
                                      intersect.pt<-c(intersect.pt,tmp)    
                                 }

                               # Find xy-coordinates of reflected subplot center
                                 rx<-2*intersect.pt[1]-cvertex.out[i,1]
                                 ry<-2*intersect.pt[2]-cvertex.out[i,2]
                                 rfl<-rbind(rfl,c(rx,ry))   
                          } 

                return(rfl)
             }

          ## Check for subplot center falling outside study area
             cvertex.out<-matrix(cvertex[!inside.owin(cvertex[,1],cvertex[,2],area),],ncol=2)

          ## Reflection method
             if(length(cvertex.out)>0){
                 # Cartesian xy-coordinates of study area vertices
                   avertex<-cbind(area$bdry[[1]]$x,area$bdry[[1]]$y)   
                   avertex<-rbind(avertex,avertex[1,])

                 # Reflect subplot centers falling outside study area 
                   cvertex.rfl<-reflect(avertex,cx,cy,cvertex.out)  
             
                 # Subplot center that originally falling inside study area
                   cvertex.in<-cvertex[inside.owin(cvertex[,1],cvertex[,2],area),]  
                                      
                 # Compile new set of subplot center with original and corrected centers
                   cvertex.cor<-rbind(cvertex.in,cvertex.rfl)
             
             }else{
                 # Boundary correction unnecessary
                   cvertex.cor<-cvertex 
             }

    return(cvertex.cor)
}
