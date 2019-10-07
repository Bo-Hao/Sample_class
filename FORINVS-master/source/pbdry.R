pbdry<-function(area,treelist,px,py,pbound){
         ### Wrapper for plot boundary overlap correction method
         ###    area: enclosed area of the dataset [spatstat object]
         ###    treelist: plot treelist [data frame]
         ###    px: x-coordinate of plot center [meter]
         ###    py: y-coordinate of plot center [meter]
         ###    pbound: plot boundary overlap correction method
         ### Output: treelist.dbl [data frame]

          ## Choice of boundary overlap correction method
	     treelist.dbl<-switch(pbound,
				  "NA"=NULL,
#		                  "walk"=bdry.walk(area,treelist,px,py)
		                  )

   return(treelist.dbl)
}
