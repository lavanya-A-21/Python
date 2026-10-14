c_s_a=lambda side_length:side_length**2
c_r_a=lambda length,width:length*width
c_t_a=lambda base,height:0.5*base*height

sqs=int(input("enter the side of square:"))
print("enter the base and height of the triangle:")
ht=int(input("height:"))
bs=int(input("base:"))

print("enter the length and breadth of the rectangle:")
l=int(input("length:"))
b=int(input("breadth:"))

square_area=c_s_a(sqs)
print("area of the square:",square_area)

triangle_area=c_t_a(bs,ht)
print("area of the triangle:",triangle_area)

rectangle_area=c_r_a(l,b)
print("area of the rectangle:",rectangle_area)
