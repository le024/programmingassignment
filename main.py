from browser import document, window, alert
import random 

def sketch(p): 
   
  #this p is needed. it will be the processing sketch itself.
  # to do things like background(0) instead do p.background(0)

    def setup():
        p.createCanvas(500, 500)
        p.background("white")
        p.rectMode(p.CENTER)
        
        
    def draw():
        p.background("#000080")
        p.noStroke()
        p.fill("red");
        p.ellipse(p.mouseX,p.mouseY,20,20);
        p.fill("green")
        p.triangle(250,40,450,500,50,500);
       
        p.fill("yellow")
        p.triangle(230, 30, 250, 1, 270, 30);
        p.triangle(195,22,305,22,250,60)
        p.triangle(210,90,230,30,255,60)
        p.triangle(285,90,270,30,250,60)
        p.textSize(20);
        p.text('HAPPY HOLIDAYS',10,30);
        p.textFont("Georgia")
        

      
    
        p.fill("pink")
        p.circle(250,250,10);
        p.circle(200,230,10);
        p.circle(260,90,10);
        p.circle(300,400,10);
        p.circle(160,470,10);
        p.circle(175,380,10);
        p.circle(400,478,10);

        p.fill("purple")
        p.circle(277,150,10)
        p.circle(230,300,10);
        p.circle(288,467,10);
        p.circle(359,354,10);

        p.fill("blue")
        p.circle(240,178,10);
        p.circle(299,303,10);
        p.circle(249,399,10);
        p.circle(113,476,10);
        


        
         
        

       
            


    
    
    def mousePressed(self):
        p.circle(0)

    

    def keyPressed(self):
      if p.key==" ":
        print("Hallo")
    

    p.setup = setup
    p.draw = draw
    p.mousePressed = mousePressed
    p.keyPressed = keyPressed
      
myp5 = window.p5.new(sketch)