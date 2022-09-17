from urllib import parse

from db_config import session as db


class GetProperties:
    """
    Gets a list of properties from database

    Attributes
    ----------
    url : str
        current request url
    query : str
        sql query string to get properties from database
    """

    BASE_QUERY_STRING = """
        SELECT A.address, A.city, A.price, A.description, A.year, C.name as status
        FROM property A
        INNER JOIN status_history B
        ON B.property_id = (
            SELECT property_id FROM status_history
            WHERE property_id = A.id
            ORDER BY update_date DESC LIMIT 1
        )
        INNER JOIN status C
        ON B.status_id = C.id
        WHERE (A.address IS NOT NULL AND A.address <> '')
        AND (C.name IN ('pre_venta', 'en_venta', 'vendido'))
    """

    def __init__(self, url) -> None:
        self.url = url
        self.query = self.BASE_QUERY_STRING

    # private methods

    def __get_url_params(self, url: str) -> dict:
        url_query = parse.urlsplit(url).query
        url_params = dict(parse.parse_qsl(url_query))
        return url_params

    def __add_filters(self, url_params: dict) -> str:
        if 'year' in url_params:
            year = url_params.get('year')
            self.query += f" AND (A.year = {year})"

        if 'city' in url_params:
            city = url_params.get('city')
            self.query += f" AND (A.city = '{city}')"

        if 'status' in url_params:
            status = url_params.get('status')
            self.query += f" AND (C.name = '{status}')"

        # gets the first created record in records with duplicate id
        self.query += " GROUP BY A.id"
        return self.query

    def __get_properties_from_db(self) -> list:
        url_params = self.__get_url_params(self.url)
        self.__add_filters(url_params)
        db.execute(self.query)
        properties = db.fetchall()
        return properties

    # public methods

    def filtered_properties(self) -> list:
        db_properties = self.__get_properties_from_db()
        return db_properties
