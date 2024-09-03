import uuid
from datetime import datetime
from typing import Any, Dict, List
import dds_loader.repository.models as model



class OrderDdsBuilder:
    def __init__(self, dict: Dict) -> None:
        self._dict = dict
        self.source_system = ""
        self.order_ns_uuid = uuid.UUID('')

    def _uuid(self, obj: Any) -> uuid.UUID:
        return uuid.uuid5(namespace=self.order_ns_uuid, name=str(obj))

    def h_user(self) -> model.H_User:
        user_id = self._dict['user']['id']
        return model.H_User(
            h_user_pk=self._uuid(user_id),
            user_id=user_id,
            load_dt=datetime.utcnow(),
            load_src=self.source_system
        )

    def h_product(self) -> List[model.H_Product]:
        products = []

        for prod_dict in self._dict['products']:
            prod_id = prod_dict['id']
            products.append(
                model.H_Product(
                    h_product_pk=self._uuid(prod_id),
                    product_id=prod_id,
                    load_dt=datetime.utcnow(),
                    load_src=self.source_system
                )
            )
        return products

    def h_category(self) -> List[model.H_Category]:
        products = self._dict["products"]
        h_categories = []
        for product in products:
            category_name = product["category"]
            h_categories.append(
                model.H_Category(
                    h_category_pk=self._uuid(category_name),
                    category_name=category_name,
                    load_dt=datetime.utcnow(),
                    load_src=self.source_system,
                )
            )
        return h_categories

    def h_restaurant(self) -> model.H_Restaurant:
        restaurant_id = self._dict["restaurant"]["id"]
        return model.H_Restaurant(
            h_restaurant_pk=self._uuid(restaurant_id),
            restaurant_id=restaurant_id,
            load_dt=datetime.utcnow(),
            load_src=self.source_system,
        )
    
    def h_order(self) -> model.H_Order:
        order_id = self._dict["id"]
        order_dt = self._dict["date"]
        return model.H_Order(
            h_order_pk=self._uuid(order_id),
            order_id=order_id,
            order_dt=order_dt,
            load_dt=datetime.utcnow(),
            load_src=self.source_system,
        )

    def l_order_product(self) -> List[model.L_Order_Product]:
        order_id = self._dict["id"]
        products = self._dict["products"]
        h_order_pk = self._uuid(order_id)
        l_order_products = []
        for product in products:
            h_product_pk = self._uuid(product["id"])
            l_order_products.append(
                model.L_Order_Product(
                    hk_order_product_pk=self._uuid(str(h_order_pk) + str(h_product_pk)),
                    h_order_pk=h_order_pk,
                    h_product_pk=h_product_pk,
                    load_dt=datetime.utcnow(),
                    load_src=self.source_system,
                )
            )
        return l_order_products


    def l_product_restaurant(self) -> List[model.L_Product_Restaurant]:
        products = self._dict["products"]
        restaurant_id = self._dict["restaurant"]["id"]
        h_restaurant_pk = self._uuid(restaurant_id)
        l_product_restaurants = []
        for product in products:
            h_product_pk = self._uuid(product["id"])
            l_product_restaurants.append(
                model.L_Product_Restaurant(
                    hk_product_restaurant_pk=self._uuid(
                        str(h_product_pk) + str(h_restaurant_pk)
                    ),
                    h_product_pk=h_product_pk,
                    h_restaurant_pk=h_restaurant_pk,
                    load_dt=datetime.utcnow(),
                    load_src=self.source_system,
                )
            )
        return l_product_restaurants

    def l_product_category(self) -> List[model.L_Product_Category]:
        products = self._dict["products"]
        l_product_categories = []
        for product in products:
            h_product_pk = self._uuid(product["id"])
            h_category_pk = self._uuid(product["category"])
            hk_product_category_pk = self._uuid(str(h_product_pk) + str(h_category_pk))
            l_product_categories.append(
                model.L_Product_Category(
                    hk_product_category_pk=hk_product_category_pk,
                    h_product_pk=h_product_pk,
                    h_category_pk=h_category_pk,
                    load_dt=datetime.utcnow(),
                    load_src=self.source_system,
                )
            )
        return l_product_categories

    def l_order_user(self) -> model.L_Order_User:
        order_id = self._dict["id"]
        h_order_pk = self._uuid(order_id)
        user_id = self._dict["user"]["id"]
        h_user_pk = self._uuid(user_id)
        return model.L_Order_User(
            hk_order_user_pk=self._uuid(str(h_order_pk) + str(h_user_pk)),
            h_order_pk=h_order_pk,
            h_user_pk=h_user_pk,
            load_dt=datetime.utcnow(),
            load_src=self.source_system,
        )

    def s_user_names(self) -> model.S_User_Names:
        user_id = self._dict["user"]["id"]
        h_user_pk = self._uuid(user_id)
        username = self._dict["user"]["name"]
        userlogin = self._dict["user"]["login"]
        return model.S_User_Names(
            h_user_pk=h_user_pk,
            username=username,
            userlogin=userlogin,
            load_dt=datetime.utcnow(),
            load_src=self.source_system,
            hk_user_names_hashdiff=self._uuid(
                str(user_id) + str(username) + str(userlogin)
            ),
        )

    def s_product_names(self) -> List[model.S_Product_Names]:
        products = self._dict["products"]
        s_product_names = []
        for product in products:
            product_id = product["id"]
            hk_product_pk = self._uuid(product_id)
            product_name = product["name"]
            s_product_names.append(
                model.S_Product_Names(
                    h_product_pk=hk_product_pk,
                    name=product_name,
                    load_dt=datetime.utcnow(),
                    load_src=self.source_system,
                    hk_product_names_hashdiff=self._uuid(
                        str(hk_product_pk) + str(product_name)
                    ),
                )
            )
        return s_product_names

    def s_restaurant_names(self) -> model.S_Restaurant_Names:
        restaurant_id = self._dict["restaurant"]["id"]
        h_restaurant_pk = self._uuid(restaurant_id)
        restaurant_name = self._dict["restaurant"]["name"]
        return model.S_Restaurant_Names(
            h_restaurant_pk=h_restaurant_pk,
            name=restaurant_name,
            load_dt=datetime.utcnow(),
            load_src=self.source_system,
            hk_restaurant_names_hashdiff=self._uuid(
                str(h_restaurant_pk) + str(restaurant_name)
            ),
        )

    def s_order_cost(self) -> model.S_Order_Cost:
        order_id = self._dict["id"]
        h_order_pk = self._uuid(order_id)
        order_cost = self._dict["cost"]
        order_payment = self._dict["payment"]
        return model.S_Order_Cost(
            h_order_pk=h_order_pk,
            cost=order_cost,
            payment=order_payment,
            load_dt=datetime.utcnow(),
            load_src=self.source_system,
            hk_order_cost_hashdiff=self._uuid(
                str(h_order_pk) + str(order_cost) + str(order_payment)
            ),
        )

    def s_order_status(self) -> model.S_Order_Status:
        order_id = self._dict["id"]
        h_order_pk = self._uuid(order_id)
        order_status = self._dict["status"]
        return model.S_Order_Status(
            h_order_pk=h_order_pk,
            status=order_status,
            load_dt=datetime.utcnow(),
            load_src=self.source_system,
            hk_order_status_hashdiff=self._uuid(str(h_order_pk) + str(order_status)),
        )