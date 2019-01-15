# Graphics How To

This graphics package can be interacted with programatically or using text commands.
To use text commands save them in a file and pass the filename as argv[1].

For each piece of the API I show the method signature and an example using the text commands.
Colors are optional to specify, the defaults are shown in the method signatures.

### Graphics Objects

* Line

   g.line((x1,y1), (x2,y2), color='blue')  
   
   lin (20,20) (180,70) yellow
   
* Square
   
   g.square((top_left_x,top_left_y), sidelength,color='green')
   
   sqr (60,110) 80 blue
   
* Circle 

   g.circle((center_x,center_y), radius, color='red')
   
   crl (100,300) 60 red
  
* Polygon

   g.polygon()
   
   Polygon has an optional boolean argument 'fill' as well as color

  * ply (250,75) (300,25) (350,75)
  * ply (250,75) (300,25) (350,75) pink
  * ply (250,75) (300,25) (350,75) fill
  * ply (250,75) (300,25) (350,75) blue fill

These methods can be displayed in the example image below:



