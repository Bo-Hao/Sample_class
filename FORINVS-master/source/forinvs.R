forinvs<-function(){
         ### Main GUI for Forest Inventory System Simulator (FORINVS)

          ## Required packages
             require(tcltk)
             require(tkrplot)

          ## Main window with title page
             winMain<-tktoplevel()
             tkwm.title(winMain,"Forest Inventory System Simulator (FORINVS)")
             image.title<-tkimage.create("photo",file="title.gif")
             imgAsLabel<-tklabel(winMain,image=image.title)
             tkpack(imgAsLabel)

          ## Main menu
             menuMain<-tkmenu(winMain)
             tkconfigure(winMain,menu=menuMain)

           # Menu 1: File System
             menuFile<-tkmenu(menuMain,tearoff=FALSE)
             tkadd(menuFile,"command",label="Close",font="Helvetica 10",command=function() tkdestroy(winMain))

           # Menu 2: Plot Design
             menuPlot<-tkmenu(menuMain,tearoff=FALSE)
             tkadd(menuPlot,"command",label="Circle",font="Helvetica 10")
             tkadd(menuPlot,"command",labe="Cluster",font="Helvetica 10") 
             tkadd(menuPlot,"command",labe="HPS",font="Helvetica 10") 
             tkadd(menuPlot,"command",label="Rectangle",font="Helvetica 10") 
             tkadd(menuPlot,"command",labe="Polygon",font="Helvetica 10") 
    
           # Menu 3: Sampling Design
             menuSamp<-tkmenu(menuMain,tearoff=FALSE)
                

           # Menu 4: Theory
             menuTheo<-tkmenu(menuMain,tearoff=FALSE)

           # Menu 5: Help
             menuHelp<-tkmenu(menuMain,tearoff=FALSE)

           # Add all menu items to main menu
             tkadd(menuMain,"cascade",label="File",menu=menuFile)
             tkadd(menuMain,"cascade",label="Plot Design",menu=menuPlot)
             tkadd(menuMain,"cascade",label="Sample Design",menu=menuSamp)
             tkadd(menuMain,"cascade",label="Theory",menu=menuTheo)
             tkadd(menuMain,"cascade",label="Help",menu=menuTheo)


   invisible()
}


