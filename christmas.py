def christmas_tree(height):
    for i in range(height):
        print(' ' * (height - i - 1) + '*' * (2 * i + 1))

    for j in range(3):  # Trunk of the tree
        print(' ' * (height - 1) + '*')

if __name__ == "__main__":
    height = int(input("Enter the height of the tree: "))
    christmas_tree(height)
