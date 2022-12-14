

from products.models import items


class Products:

    def list(self, *args, **kwargs):              # To List all items or objects
        all_products = items
        if "category" in kwargs:
            cat = kwargs.get("category")
            all_products = [p for p in all_products if p.get("category")==cat]
        return all_products

    def retrieve(self,*args,**kwargs):            # To list a specific item or object
        id = kwargs.get("id")
        item=[i for i in items if i.get("id")==id]
        return item

    def destroy(self,*args,**kwargs):             # To delete any specified item or object
        id = kwargs.get("id")
        item = [i for i in items if i.get("id")==id][0]
        items.remove(item)
        return item

    def create(self,*args,**kwargs):              # To create or add or append a new item to the list
        data = kwargs.get("data")
        items.append(data)
        return data

    def update(self,*args,**kwargs):
        id = kwargs.get("id")
        data = kwargs.get("data")
        instance = [i for i in items if i.get("id")==id][0]
        instance.update(data)
        return instance

p = Products()
# print(p.list(category="electronics"))
# print(p.retrieve(id=20))
# print(p.destroy(id=1))

data = {
    "price": 3500,
    "description": "Stylish watch for men"
    }

# print(p.create(data=data))
print(p.update(id=1,data=data))

