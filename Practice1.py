#take  input from user loacation and aks user to show or save image if save image
#then also take file location to save and saveit else show it 

import cv2

# Step 1: Take image path from user
img_path = input("Enter the image file path: ")

# Step 2: Read image
img = cv2.imread(img_path)

if img is None:
    print("Error: Could not read the image. Check file path!")
else:
    # Step 3: Ask user what to do
    choice = input("Do you want to (s)ave or (d)isplay the image? (s/d): ").lower()

    if choice == "s":
        # Step 4: Take save location
        save_path = input("Enter the file path to save (e.g. output.jpg): ")
        cv2.imwrite(save_path, img)
        print(f"Image saved at {save_path}")
    
    elif choice == "d":
        # Step 5: Show the image
        cv2.imshow("Image", img)
        cv2.waitKey(0)   # wait until key press
        cv2.destroyAllWindows()
    
    else:
        print("Invalid choice. Please enter 's' to save or 'd' to display.")
