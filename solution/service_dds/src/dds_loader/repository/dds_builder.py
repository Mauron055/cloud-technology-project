import uuid
from datetime import datetime
from typing import Any, Dict, List
import dds_loader.repository.models as model


class OrderDdsBuilder:
    def __init__(self, data: Dict) -> None:
        self._data = data
        self.source_system = "OrderSource"
        self.order_ns_uuid = uuid.uuid5(uuid.NAMESPACE_DNS, "order_data")

    def _generate_uuid(self, obj: Any) -> uuid.UUID:
        return uuid.uuid5(namespace=self.order_ns_uuid, name=str(obj))

    def h_user(self) -> model.H_User:
        user_id = self._data["user"]["id"]
        return model.H_User(
            h_user_pk=self._generate_uuid(user_id),
            user_id=user_id,
            load_dt=datetime.utcnow(),
            load_src=self.source_system,
        )

    def h_product(self) -> List[model.H_Product]:
        products = []
        for product_data in self._data["products"]:
            product_id = product_data["id"]
            products.append(
                model.H_Product(
                    h_product_pk=self._generate_uuid(product_id),
                    product_id=product_id,
                    load_dt=datetime.utcnow(),
                    load_src=self.source_system,
                )
            )
        return products

    def h_category(self) -> List[model.H_Category]:
        categories = []
        for product_data in self._data["products"]:
            category_name = product_data["category"]
            categories.append(
                model.H_Category(
                    h_category_pk=self._generate_uuid(category_name),
                    category_name=category_name,
                    load_dt=datetime.utcnow(),
                    load_src=self.source_system,
                )
            )
        return categories

    def h_restaurant(self) -> model.H_Restaurant:
        restaurant_id = self._data["restaurant"]["id"]
        return model.H_Restaurant(
            h_restaurant_pk=self._generate_uuid(restaurant_id),
            restaurant_id=restaurant_id,
            load_dt=datetime.utcnow(),
            load_src=self.source_system,
        )

    def h_order(self) -> model.H_Order:
        order_id = self._data["id"]
        order_dt = datetime.strptime(self._data["date"], "%Y-%m-%d %H:%M:%S")
        return model.H_Order(
            h_order_pk=self._generate_uuid(order_id),
            order_id=order_id,
            order_dt=order_dt,
            load_dt=datetime.utcnow(),
            load_src=self.source_system,
        )

    def l_order_product(self) -> List[model.L_Order_Product]:
        order_id = self._data["id"]
        h_order_pk = self._generate_uuid(order_id)
        order_products = []
        for product_data in self._data["products"]:
            h_product_pk = self._generate_uuid(product_data["id"])
            order_products.append(
                model.L_Order_Product(
                    hk_order_product_pk=self._generate_uuid(
                        f"{h_order_pk}_{h_product_pk}"
                    ),
                    h_order_pk=h_order_pk,
                    h_product_pk=h_product_pk,
                    load_dt=datetime.utcnow(),
                    load_src=self.source_system,
                )
            )
        return order_products

    def l_product_restaurant(self) -> List[model.L_Product_Restaurant]:
        restaurant_id = self._data["restaurant"]["id"]
        h_restaurant_pk = self._generate_uuid(restaurant_id)
        product_restaurants = []
        for product_data in self._data["products"]:
            h_product_pk = self._generate_uuid(product_data["id"])
            product_restaurants.append(
                model.L_Product_Restaurant(
                    hk_product_restaurant_pk=self._generate_uuid(
                        f"{h_product_pk}_{h_restaurant_pk}"
                    ),
                    h_product_pk=h_product_pk,
                    h_restaurant_pk=h_restaurant_pk,
                    load_dt=datetime.utcnow(),
                    load_src=self.source_system,
                )
            )
        return product_restaurants

    def l_product_category(self) -> List[model.L_Product_Category]:
        product_categories = []
        for product_data in self._data["products"]:
            h_product_pk = self._generate_uuid(product_data["id"])
            h_category_pk = self._generate_uuid(product_data["category"])
            product_categories.append(
                model.L_Product_Category(
                    hk_product_category_pk=self._generate_uuid(
                        f"{h_product_pk}_{h_category_pk}"
                    ),
                    h_product_pk=h_product_pk,
                    h_category_pk=h_category_pk,
                    load_dt=datetime.utcnow(),
                    load_src=self.source_system,
                )
            )
        return product_categories

    def l_order_user(self) -> model.L_Order_User:
        order_id = self._data["id"]
        h_order_pk = self._generate_uuid(order_id)
        user_id = self._data["user"]["id"]
        h_user_pk = self._generate_uuid(user_id)
        return model.L_Order_User(
            hk_order_user_pk=self._generate_uuid(f"{h_order_pk}_{h_user_pk}"),
            h_order_pk=h_order_pk,
            h_user_pk=h_user_pk,
            load_dt=datetime.utcnow(),
            load_src=self.source_system,
        )

    def s_user_names(self) -> model.S_User_Names:
        user_id = self._data["user"]["id"]
        h_user_pk = self._generate_uuid(user_id)
        username = self._data["user"]["name"]
        userlogin = self._data["user"]["login"]
        return model.S_User_Names(
            h_user_pk=h_user_pk,
            username=username,
            userlogin=userlogin,
            load_dt=datetime.utcnow(),
            load_src=self.source_system,
            hk_user_names_hashdiff=self._generate_uuid(
                f"{user_id}_{username}_{userlogin}"
            ),
        )

    def s_product_names(self) -> List[model.S_Product_Names]:
        product_names = []
        for product_data in self._data["products"]:
            product_id = product_data["id"]
            h_product_pk = self._generate_uuid(product_id)
            product_name = product_data["name"]
            product_names.append(
                model.S_Product_Names(
                    h_product_pk=h_product_pk,
                    name=product_name,
                    load_dt=datetime.utcnow(),
                    load_src=self.source_system,
                    hk_product_names_hashdiff=self._generate_uuid(
                        f"{h_product_pk}_{product_name}"
                    ),
                )
            )
        return product_names

    def s_restaurant_names(self) -> model.S_Restaurant_Names:
        restaurant_id = self._data["restaurant"]["id"]
        h_restaurant_pk = self._generate_uuid(restaurant_id)
        restaurant_name = self._data["restaurant"]["name"]
        return model.S_Restaurant_Names(
            h_restaurant_pk=h_restaurant_pk,
            name=restaurant_name,
            load_dt=datetime.utcnow(),
            load_src=self.source_system,
            hk_restaurant_names_hashdiff=self._generate_uuid(
                f"{h_restaurant_pk}_{restaurant_name}"
            ),
        )

    def s_order_cost(self) -> model.S_Order_Cost:
        order_id = self._data["id"]
        h_order_pk = self._generate_uuid(order_id)
        order_cost = self._data["cost"]
        order_payment = self._data["payment"]
        return model.S_Order_Cost(
            h_order_pk=h_order_pk,
            cost=order_cost,
            payment=order_payment,
            load_dt=datetime.utcnow(),
            load_src=self.source_system,
            hk_order_cost_hashdiff=self._generate_uuid(
                f"{h_order_pk}_{order_cost}_{order_payment}"
            ),
        )

    def s_order_status(self) -> model.S_Order_Status:
        order_id = self._data["id"]
        h_order_pk = self._generate_uuid(order_id)
        order_status = self._data["status"]
        return model.S_Order_Status(
            h_order_pk=h_order_pk,
            status=order_status,
            load_dt=datetime.utcnow(),
            load_src=self.source_system,
            hk_order_status_hashdiff=self._generate_uuid(
                f"{h_order_pk}_{order_status}"
            ),
        )
