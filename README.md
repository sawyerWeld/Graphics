# Graphics How To

This graphics package can be interacted with programatically or using text commands.
To use text commands save them in a file and pass the filename as argv[1].

For each piece of the API I show the method signature and an example using the text commands.
Colors are optional to specify, the defaults are shown in the method signatures.

### Graphics Objects

* Line
```
g.line((x1,y1), (x2,y2), color='blue')  
   
lin (20,20) (180,70) yellow
```   
* Square
```
g.square((top_left_x,top_left_y), sidelength,color='green')

sqr (60,110) 80 blue
```   
* Circle 
```
g.circle((center_x,center_y), radius, color='red')
   
crl (100,300) 60 red
``` 
* Polygon
```
g.polygon([Vertex List], color='purple', fill='false')
```
   Polygon has an optional boolean argument 'fill' as well as color
```
ply (250,75) (300,25) (350,75)
ply (250,75) (300,25) (350,75) pink
ply (250,75) (300,25) (350,75) fill
ply (250,75) (300,25) (350,75) blue fill
```
These methods can be displayed in the example image below:

![alt text](https://github.com/sawyerWeld/Graphics/blob/master/images/image_1.PNG)
```
# Example_1.txt
lin (20,20) (180,70) yellow
sqr (60,110) 80 blue
crl (100,300) 60 red
ply (250,75) (300,25) (350,75) (350,175) (300,125) (250,175) green
ply (250,250) (300,200) (350,250) (350,350) (300,300) (250,350) purple fill
```
This can be run with the command
```
python graph.py Example_1.txt
```

### Groupings

* group() - initializes an empty group
* add(graphics_object) - adds an object to the group
* add_multiple([list]) - adds a list of objects to the group
* rm(graphics_object) - removes an object from the group
 
 There is only one group method used in the text file interface:
 ```
 grp obj1 obj2 obj3
 ```
 This groups the first three objects created into a group. Objects are never given a name when made, but instead assigned a number. The first object made is 'obj1'. In the case of the image above, this would group the line, square, and circle. Assuming this is the first grouping made, it can be referred to as 'grp1'. Subsequent groupings are 'grp2', 'grp3', etc.

### Transformations

* Translation  
Translate the target object or group of object in the x and y directions
```
translate(dx, dy)
tra obj1 50 50
tra grp1 50 50
```
* Rotation  
Rotates the target object or group of objects clockwise about of point. Angle is input in **degrees**.
The default focus is (200,200) because the default window size is 400 x 400.
```
rotate(45, focus=(200,200))
rot obj1 45
rot grp1 40 (100,100)
```
* Scale
Scales the target object or group of objects. Accepts non-integer values.
```
scale(2.0)  # Double in size
scale(0.5)  # Halve the size
scl obj1 2.0
scl grp1 0.5
```

### Text

Text is special graphics object which is intentionally not acted on by transformations
```
text((100,10), 'hello world', color='white')
txt (100,10) hello_world white
```
The valid characters are:
```
abcdefghijklmnopqrstuvwxyz()./ and space
```
Spaces signal the end of a parameter in text commands, so '\_' is used instead
```
txt (0,0) hello_world # 'hello world'
```

