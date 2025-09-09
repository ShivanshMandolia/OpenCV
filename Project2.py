#take file location as input and give option wheter to draw line or circle  or rectangle and also
#take input of that particular field and give otpn of saving and displaying


import cv2

# Step 1: Take image path input
file_path = input("Enter the image file path: ").strip()
img = cv2.imread(file_path)

if img is None:
    print("Error: Could not load image. Check file path!")
    exit()

print("\nChoose a shape to draw:")
print("1. Line")
print("2. Rectangle")
print("3. Circle")

choice = int(input("Enter choice (1/2/3): "))

# Step 2: Drawing shapes
if choice == 1:
    print("Enter coordinates for Line")
    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))
    x2 = int(input("Enter x2: "))
    y2 = int(input("Enter y2: "))
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 3)

elif choice == 2:
    print("Enter coordinates for Rectangle")
    x1 = int(input("Enter top-left x1: "))
    y1 = int(input("Enter top-left y1: "))
    x2 = int(input("Enter bottom-right x2: "))
    y2 = int(input("Enter bottom-right y2: "))
    cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 3)

elif choice == 3:
    print("Enter details for Circle")
    x = int(input("Enter center x: "))
    y = int(input("Enter center y: "))
    r = int(input("Enter radius: "))
    cv2.circle(img, (x, y), r, (0, 0, 255), 3)

else:
    print("Invalid choice!")
    exit()

# Step 3: Save or Display
print("\nDo you want to:")
print("1. Show Image")
print("2. Save Image")

action = int(input("Enter choice (1/2): "))

if action == 1:
    cv2.imshow("Modified Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
elif action == 2:
    save_path = input("Enter file path to save (e.g., output.jpg): ").strip()
    cv2.imwrite(save_path, img)
    print(f"Image saved successfully at {save_path}")
else:
    print("Invalid option!")
