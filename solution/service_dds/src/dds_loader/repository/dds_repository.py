from datetime import datetime
from lib.pg import PgConnect
import dds_loader.repository.models as model


class DdsRepository:
    def __init__(self, db: PgConnect) -> None:
        self._db = db

    def _insert_record(self, table_name: str, params: Dict) -> None:
        with self._db.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    f"""
                    insert into dds.{table_name} ({','.join(params.keys())})
                    values ({','.join(['%(' + key + ')s' for key in params.keys()])})
                    on conflict ({','.join([key for key in params.keys() if 'pk' in key])}) do nothing;
                    """,
                    params,
                )

    def h_user_insert(self, user: model.H_User) -> None:
        self._insert_record("h_user", user.dict())

    def h_product_insert(self, product: model.H_Product) -> None:
        self._insert_record("h_product", product.dict())

    def h_category_insert(self, category: model.H_Category) -> None:
        self._insert_record("h_category", category.dict())

    def h_restaurant_insert(self, restaurant: model.H_Restaurant) -> None:
        self._insert_record("h_restaurant", restaurant.dict())

    def h_order_insert(self, order: model.H_Order) -> None:
        self._insert_record("h_order", order.dict())

    def l_order_product_insert(self, order_product: model.L_Order_Product) -> None:
        self._insert_record("l_order_product", order_product.dict())

    def l_product_restaurant_insert(
        self, product_restaurant: model.L_Product_Restaurant
    ) -> None:
        self._insert_record("l_product_restaurant", product_restaurant.dict())

    def l_product_category_insert(
        self, product_category: model.L_Product_Category
    ) -> None:
        self._insert_record("l_product_category", product_category.dict())

    def l_order_user_insert(self, order_user: model.L_Order_User) -> None:
        self._insert_record("l_order_user", order_user.dict())

    def s_user_names_insert(self, user_names: model.S_User_Names) -> None:
        self._insert_record("s_user_names", user_names.dict())

    def s_product_names_insert(self, product_names: model.S_Product_Names) -> None:
        self._insert_record("s_product_names", product_names.dict())

    def s_restaurant_names_insert(
        self, restaurant_names: model.S_Restaurant_Names
    ) -> None:
        self._insert_record("s_restaurant_names", restaurant_names.dict())

    def s_order_cost_insert(self, order_cost: model.S_Order_Cost) -> None:
        self._insert_record("s_order_cost", order_cost.dict())

    def s_order_status_insert(self, order_status: model.S_Order_Status) -> None:
        self._insert_record("s_order_status", order_status.dict())
