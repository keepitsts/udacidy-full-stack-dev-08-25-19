#Import Dependencies
from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, StoreItem

app = Flask(__name__)

engine = create_engine('sqlite:///storeitemsinventory.db')
Base.metadata.bind = engine

#Create a Session
DBSession = sessionmaker(bind=engine)
session = DBSession()



#JSON API Endpoints

#@app.route('/')
@app.route('/api/v1.0/category/JSON')
def categoriesJSON():
    categories = session.query(Category).all()
    return jsonify(categories=[c.serialize for c in categories])


@app.route('/api/v1.0/category/storeItems/JSON')
def showStoreItemJSON():
    storeItem = session.query(StoreItem).all()
    return jsonify(storeItem=[s.serialize for s in storeItem])


@app.route('/api/v1.0/category/<int:category_id>inventory/JSON')
def showCategoryItemsJSON(category_id):
    category = session.query(StoreItem).filter_by(id=category_id).one()
    items = session.query(StoreItem).filter_by(category_id=category_id).all()
    
    return jsonify(StoreItems=[i.serialize for i in items])

@app.route('/api/v1.0/category/<int:category_id>/inventory/<int:inventory_id>/JSON')
def storeItemsJSON(category_id, inventory_id):
    store_item = session.query(StoreItem).all()
    return jsonify(store_item=store_item.serialize)

@app.route('/api/v1.0/oneItem')
def viewOneItem(item_id):
    view_item = session.query(StoreItem).one()
    return jsonify(view_item=view_item.serialize)



"""
The following routes and functions pull data from the Store Items Inventory database
and inserts the data into html templates.
"""

#Categories

#Show all categories.
@app.route('/')
@app.route('/catalog/')
def showCategories():
    categories = session.query(Category).all()
    #return "These are the categories."
    return render_template('categories.html', categories=categories)




#Public Catalog
#@app.route('/')
@app.route('/catalog/public/')
def publicCatalog():
    categories = session.query(Category).all()
    return render_template('publicCatalog.html', categories=categories)



#Create a new category.
@app.route('/catalog/category/new/', methods=['GET', 'POST'])
def newCategory():
    if request.method == 'POST':
        newCategory = Category(name=request.form['name'])
        session.add(newCategory)
        session.commit()
        flash("New category created!")
        return redirect(url_for('showCategories'))
    else:
        return render_template('newCategory.html')


#Edit a category.
@app.route('/catelog/<int:category_id>/edit/', methods=['GET','POST'])
def editCategory(category_id):
    editedCategory = session.query(
        Category).filter_by(id=category_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedCategory.name = request.form['name']
            session.add(editedCategory)
            session.commit()
            flash("Category has been edited")
            return redirect(url_for('showCategories'))
    else:
        return render_template('editCategory.html', category=editedCategory)        


#Delete a category.
@app.route('/catalog/category/<int:category_id>/delete/', methods=['GET', 'POST'])
def deleteCategory(category_id):
    categoryToDelete = session.query(Category).filter_by(id=category_id).one()
    if request.method == 'POST':
        session.delete(categoryToDelete)
        session.commit()
        flash("Category has been deleted!")
        return redirect(url_for('showCategories', category_id=category_id))
    else:
        return render_template('deleteCategory.html', category=categoryToDelete)



#Items

#This function shows all the items in a catagory.
@app.route('/catalog/category/<int:category_id>/')
@app.route('/catalog/category/<int:category_id>/inventory')
def showItems(category_id):
    category = session.query(Category).filter_by(id=category_id).one()
    items = session.query(StoreItem).filter_by(category_id=category_id).all()
    return render_template('items.html', category=category, items=items)


#List of items for the public catalog.
@app.route('/catalog/public/<int:category_id>/')
@app.route('/catalog/category/public/<int:category_id>/inventory')
def showItemsPublic(category_id):
    category = session.query(Category).filter_by(id=category_id).one()
    items = session.query(StoreItem).filter_by(category_id=category_id).all()
    return render_template('publicCatalogitems.html', items=items, category=category)
"""

#This function returns a list of the item names.
@app.route('/catalog/<int:category_id>/')
@app.route('/catalog/category/<int:category_id>/itemlist')
def listNames(category_id):
    category = session.query(Category).filter_by(id=category_id).one()
    items = session.query(StoreItem).filter_by(category_id=category_id).all()
    return render_template('viewItems.html', items=items, category=category)
"""

#This function allows the user to view a single item.
@app.route('/catalog/category/<int:category_id>/<int:item_id>/item')
def viewItem(category_id,item_id):
    category = session.query(Category).filter_by(id=category_id).one()
    item = session.query(StoreItem).filter_by(id=item_id).one()
    return render_template("viewItem.html",category=category, item=item)

@app.route('/catalog/public/category/<int:category_id>/<int:item_id>/item')
def viewItemPublic(category_id,item_id):
    category = session.query(Category).filter_by(id=category_id).one()
    item = session.query(StoreItem).filter_by(id=item_id).one()
    return render_template("viewItemPublic.html",category=category, item=item)


#Create a new store item.
@app.route('/catalog/category/<int:category_id>/new/', methods=['GET','POST'])
def newStoreItem(category_id):
    categories = session.query(Category).all()
    if request.method == 'POST':
        newItem = StoreItem(
            name=request.form['name'], 
            author=request.form['author'],
            genre=request.form['genre'],
            price=request.form['price'], 
            description=request.form['description'])

        session.add(newItem)
        session.commit()
        flash("New item has been created!")

        return redirect(url_for('showItems'), category_id=category_id)

    else:
        return render_template('newItem.html', category_id=category_id)

#Edit a store item.
@app.route('/catalog/category/<int:category_id>/<int:item_id>/edit/', methods=['GET', 'POST'])
def editStoreItem(category_id, item_id):
    editedItem = session.query(StoreItem).filter_by(id=item_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
        if request.form['author']:
            editedItem.author = request.form['author']
        if request.form['genre']:
            editedItem.genre = request.form['genre']
        if request.form['price']:
            editedStoreItem.price = request.form['price']
        if request.form['description']:
            editedItem.description = request.form['description']

        session.add(editedItem)
        session.commit()
        flash("Item has been edited!")
        return redirect(url_for('showItems', category_id=category_id), item=editedStoreItem)

    else:
        #catagories = session.query(Catagory).all()
        return render_template('editItem.html', category_id=category_id,item=editedItem)


#Delete a store item.
@app.route('/catalog/category/<int:category_id>/inventory/<int:inventory_id>/delete/', methods=['GET', 'POST'])
def deleteStoreItem(category_id, inventory_id):
    itemToDelete = session.query(StoreItem).filter_by(id=inventory_id).one()
    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        flash("Item has been deleted!")
        return redirect(url_for('showItems', category_id=category_id))
    else:
        return render_template('deleteItem.html', item=itemToDelete)

#Starting the Flask Server

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='localhost', port=5000)
