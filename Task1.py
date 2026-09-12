import math

# Take input from user
Wpx = int(input("Enter horizontal pixels: "))
Hpx = int(input("Enter vertical pixels: "))
Dinches = float(input("Enter screen diagonal in inches: "))

# Total pixels
total_pixels = Wpx * Hpx

# Aspect ratio
gcd = math.gcd(Wpx, Hpx)
W = Wpx // gcd
H = Hpx // gcd

# Calculate DPI
diagonal_pixels = math.sqrt(Wpx**2 + Hpx**2)
dpi = diagonal_pixels / Dinches

# Display density
if dpi < 100:
    density = "Low Density (Standard Monitor)"
elif dpi <= 200:
    density = "Medium Density (HD Display)"
else:
    density = "High Density (Retina / Mobile)"

# Show results
print("\nTotal Pixel Count:", total_pixels)
print("Aspect Ratio:", W, ":", H)
print("DPI/PPI:", round(dpi, 2))
print("Display Density:", density)