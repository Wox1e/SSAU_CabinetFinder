## graph.py

Модуль для работы с базой данных Neo4j.

### Класс Neo4jConnection

Основной класс для управления подключением к Neo4j и выполнения запросов.

#### Методы:

##### `__init__(uri, user, password)`
Инициализация подключения к Neo4j.
- **Параметры:**
  - `uri` (str): URI базы данных Neo4j
  - `user` (str): Имя пользователя
  - `password` (str): Пароль

##### `close()`
Закрытие соединения с драйвером Neo4j.

##### `query(query, db=None)`
Выполнение Cypher-запроса к базе данных.
- **Параметры:**
  - `query` (str): Cypher-запрос
  - `db` (str, optional): Имя базы данных
- **Возвращает:** список результатов запроса

### Вспомогательные функции

##### `dict_to_str(d)`
Преобразование словаря в строку, совместимую с Neo4j.
- **Параметры:**
  - `d` (dict): Словарь для преобразования
- **Возвращает:** строковое представление словаря

### Функции для работы с графом

##### `create_node(category: str, properties: dict) -> str`
Создание нового узла в базе данных.
- **Параметры:**
  - `category`: Метка/категория узла
  - `properties`: Свойства узла
- **Возвращает:** ID созданного элемента

##### `create_OneDirectionalEdge(sourceNode_elementID: str, destNode_elementID: str, RelationType: str)`
Создание направленного ребра между узлами.
- **Параметры:**
  - `sourceNode_elementID`: ID исходного узла
  - `destNode_elementID`: ID целевого узла
  - `RelationType`: Тип отношения

##### `get_Node(elementId: str)`
Получение узла по его ID.
- **Параметры:**
  - `elementId`: ID узла
- **Возвращает:** данные узла

##### `get_path_between_nodes(sourceNode_elementID: str, destNode_elementID: str)`
Поиск кратчайшего пути между узлами.
- **Параметры:**
  - `sourceNode_elementID`: ID начального узла
  - `destNode_elementID`: ID конечного узла
- **Возвращает:** список узлов на пути

##### `get_all_nodes()`
Получение всех узлов из базы данных.
- **Возвращает:** список всех узлов

##### `delete_Node(elementID: str) -> bool`
Удаление узла по его ID.
- **Параметры:**
  - `elementID`: ID узла для удаления
- **Возвращает:** False при ошибке

##### `add_properties_to_node(elementID: str, properties: dict) -> bool`
Добавление или обновление свойств узла.
- **Параметры:**
  - `elementID`: ID узла
  - `properties`: Словарь с новыми свойствами
- **Возвращает:** False при ошибке