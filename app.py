import csv
import os #refer to notes in the course repo regarding the os module.

def menu(username="iriskhu", products_count=100):
    # this is a multi-line string, also using preceding `f` for string interpolation
    menu = f"""
    -----------------------------------
    INVENTORY MANAGEMENT APPLICATION
    -----------------------------------
    Welcome {username}!
    There are {products_count} products in the database.
        operation | description
        --------- | ------------------
        'List'    | Display a list of product identifiers and names.
        'Show'    | Show information about a product.
        'Create'  | Add a new product.
        'Update'  | Edit an existing product.
        'Destroy' | Delete an existing product.
        'Reset'   | Reset the CSV file.

    Please select an operation: """ # end of multi- line string. also using string interpolation
    return menu

def read_products_from_file(filename = "products.csv"):
    filepath = os.path.join(os.path.dirname(__file__), "db", filename)
    print(f"READING PRODUCTS FROM FILE: '{filepath}'")
    products = [] # the next commands are to open the file and populate the products list with product dictionaries)
    with open(filepath, "r") as csv_file: # to open file "filepath"
        reader = csv.DictReader(csv_file) # to assume your CSV has headers
        for ordered_dict in reader:
            products.append(dict(ordered_dict)) #adding stuff to the row
    return products

def write_products_to_file(filename="products.csv", products=[]):
    filepath = os.path.join(os.path.dirname(__file__), "db", filename)
    #print(f"OVERWRITING CONTENTS OF FILE: '{filepath}' \n ... WITH {len(products)} PRODUCTS")
    print ("Writing to", filepath)
    with open(filepath, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["id", "name", "aisle", "department", "price"])
        writer.writeheader()
        for p in products:
            writer.writerow({"id": p["id"], "name": p["name"], "aisle": p["aisle"], "department": p["department"], "price": p["price"]})

def reset_products_file(filename="products.csv", from_filename="products_default.csv"):
    print("RESETTING DEFAULTS")
    products = read_products_from_file(from_filename)
    write_products_to_file(filename, products)
    quit()


def run():
#the run function here is to specify which function is going wrong

    # First, read products from file...
    products = read_products_from_file()

    # Then, prompt the user to select an operation...
    number_of_products = len(products)
    my_menu = menu(username="iriskhu", products_count=number_of_products)
    operation = input(my_menu)
    print("YOU CHOSE: " + operation)

    # Then, handle selected operation: "List", "Show", "Create", "Update", "Destroy" or "Reset"...
    operation = operation.title() #this way, you can type "List", "list", or "LIST".


    if operation == "List":
        print("----------------------")
        print("LISTING PRODUCTS") #use for loop for "List"
        print("----------------------")
        for p in products: #for each one in producsts, do something with it
            print("   " + p["id"] + ". " + p["name"])

    elif operation == "Show":
        print("----------------------")
        print("SHOWING A PRODUCT")
        print("----------------------")
        product_id = input("Hey, what's identifier of the product you want to display? ")
        matching_products = [p for p in products if (p["id"]) == product_id] #list comprehension!!
        matching_product = matching_products[0]
        print(matching_product)

    elif operation == "Create":
        print("----------------------")
        print("CREATING A PRODUCT")
        print("----------------------")
        new_id = input ("please input the product id: ")
        new_name = input ("please input the product name: ")
        new_aisle = input ("please input the product aisle: ")
        new_dept = input ("please input the product department: ")
        new_price = input ("please input the product price: ")

        new_product = {
            "id": new_id,
            "name": new_name,
            "aisle": new_aisle,
            "department": new_dept,
            "price": new_price
        }
        products.append(new_product)
        print("----------------------")
        print ("CREATING A NEW PRODUCT: ", new_product)
        print("----------------------")

    elif operation == "Update":
        product_id = input("Hey, what's the identifier of the product you want to update? ")
        product_name = input ("please input the product's new name: ")
        product_aisle = input ("please input the product's new aisle: ")
        product_dept = input ("please input the product's new department: ")
        product_price = input ("please input the product's new price: ")

        updated_product = {
            "id": product_id,
            "name": product_name,
            "aisle": product_aisle,
            "department": product_dept,
            "price": product_price
        }
        products.append(updated_product)
        print("----------------------")
        print ("UPDATED PRODUCT: ", updated_product)
        print("----------------------")

    elif operation == "Destroy":
        product_id = input("Hey, what's the identifier of the product you want to destroy? ")
        matching_products = [p for p in products if p["id"] == product_id]
        matching_product = matching_products[0]
        del products[products.index(matching_product)]
        print("----------------------")
        print("DESTROYING A PRODUCT")
        print("----------------------")

    elif operation == "Reset":
        reset_products_file()

    else:
        print("----------------------")
        print("Oops, unrecognized operation, please select one of 'List', 'Show', 'Create', 'Update', 'Destroy', 'Reset'.")
        print("----------------------")
    # Finally, save products to file so they persist after script is done...
    write_products_to_file(products=products)

# only prompt the user for input if this script is run from the command-line
# this allows us to import and test this application's component functions

if __name__ == "__main__":
    run()
