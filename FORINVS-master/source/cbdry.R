cbdry<-function(area,cx,cy,cvertex,cbound){
         ### Wrapper for cluster boundary overlap correction method
         ###    area: enclosed area of the dataset [spatstat object]
         ###    cx: x-coordinate of cluster center [meter]
         ###    cy: y-coordinate of cluster center [meter]
         ###    cvertex: Cartesian xy-coordinates of subplot centers [meter]
         ###    cbound: cluster boundary overlap correction method

          ## Choice of boundary overlap correction method
             cvertex.cor<-switch(cbound,
			         "NA"=cvertex,
    		                 "reflect"=cbdry.reflect(area,cx,cy,cvertex)
		                 )

   return(cvertex.cor)
}
