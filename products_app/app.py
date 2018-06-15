import csv
import os ## reference (partial sample codes): https://github.com/prof-rossetti/nyu-info-2335-201805/blob/master/notes/programming-languages/python/modules/os.md.

def menu(username="iriskhu", products_count=100):
    ## this is a multi-line string, also using preceding `f` for string interpolation---Prof.'s notes
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

    Please select an operation: """ ## end of multi- line string. also using string interpolation---Prof.'s notes
    return menu

def read_products_from_file(filename = "products.csv"):
    filepath = os.path.join(os.path.dirname(__file__), "db", filename)
    print(f"READING PRODUCTS FROM FILE: '{filepath}'")
    products = [] ## the next commands are to open the file and populate the products list with product dictionaries)
    with open(filepath, "r") as csv_file: ## to open file "filepath"
        reader = csv.DictReader(csv_file) ## to assume your CSV has headers
        for ordered_dict in reader:
            products.append(dict(ordered_dict)) ## append.() function: adding stuff to the row
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
## the run function here is to specify which function is going wrong

    ## First, read products from file...
    products = read_products_from_file()

    ## Then, prompt the user to select an operation...
    number_of_products = len(products) ## reference: in-class workshop
    my_menu = menu(username="iriskhu", products_count=number_of_products)
    operation = input(my_menu)
    print("YOU CHOSE: " + operation)

    ## Then, handle selected operation: "List", "Show", "Create", "Update", "Destroy" or "Reset"...

    operation = operation.title() ## reference: in-class workshop
    ## this way, you can type "List", "list", or "LIST".


    if operation == "List":
        print("----------------------")
        print("LISTING ALL PRODUCTS")
        print("----------------------")
        for p in products:
            print("   " + p["id"] + ". " + p["name"])


    elif operation == "Show":
        print("----------------------")
        print("SHOWING A PRODUCT")
        print("----------------------")
        product_id = input("Hey, what's identifier of the product you want to display? ")
        matching_products = [p for p in products if (p["id"]) == product_id] #list comprehension!!
        if not matching_products: ## reference: https://stackoverflow.com/questions/16739555/python-if-not-syntax?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
            print("Oops, product doesn't exist. Please try again.")
        else:
            matching_product = matching_products[0]
            for m in matching_products:
                print("----------------------")
                print ("HERE IS THE PRODUCT:")
                print("----------------------")
                print ("{'id': " + product_id + ", 'name': " + m["name"] + ", 'aisle': " + m["aisle"] + ", 'department': " + m["department"] + ", 'price': $" + m["price"] + "}")


    elif operation == "Create":
        print("----------------------")
        print("CREATING A NEW PRODUCT")
        print("----------------------")
        new_id = int(products[-1]["id"]) + 1 ## new id # = the last existing id # plus 1
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
        print ("----------------------")
        print ("CREATED PRODUCT: ")
        print ("----------------------")
        print (new_product)


    elif operation == "Update":
        print("----------------------")
        print ("UPDATED A PRODUCT:")
        print("----------------------")
        product_id = input("Hey, what's identifier of the product you want to update? ")
        selected_products = [p for p in products if (p["id"]) == product_id]
        if not selected_products:
            print("Oops, product doesn't exist. Please try again.")
        else:
            selected_product = selected_products[0]
            selected_product["name"] = input ("please input the product's new name: ")
            selected_product["aisle"] = input ("please input the product's new aisle: ")
            selected_product["department"] = input ("please input the product's new department: ")
            selected_product["price"] = input ("please input the product's new price: ")

            selected_product = {
                "updated id": product_id,
                "updated name": selected_product["name"],
                "updated aisle": selected_product["aisle"],
                "updated department": selected_product["department"],
                "updated price": selected_product["price"]
                }

            print("----------------------")
            print ("UPDATED PRODUCT:")
            print("----------------------")
            print ("{'id': " + selected_product["updated id"] + ", "+ "'updated name': " + selected_product["updated name"] + ", 'updated aisle': " + selected_product["updated aisle"] + ", 'updated department': " + selected_product["updated department"] + ", 'updated price': $" + selected_product["updated price"] + "}")


    elif operation == "Destroy":
        print("----------------------")
        print("DESTROYING A PRODUCT:")
        print("----------------------")
        product_id = input("Hey, what's the identifier of the product you want to destroy? ")
        destroying_products = [p for p in products if p["id"] == product_id]
        if not destroying_products: ## reference: https://stackoverflow.com/questions/16739555/python-if-not-syntax?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
            print("Oops, product doesn't exist. Please try again.")
        else:
            destroying_product = destroying_products[0]
            del products[products.index(destroying_product)]
            print("----------------------")
            print("DESTROYED THIS PRODUCT:")
            print("----------------------")
            print(destroying_product)


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
