import redis

class TodoCRUD:
    def __init__(self):
        self.r = redis.Redis(host='localhost', port=6379, db=0)

    def create_todo(self, todo_id, todo_text):
        self.r.set(todo_id, todo_text)
        print(f'Todo creado: {todo_id} - {todo_text}')

    def read_all_todos(self):
        todos = self.r.keys()
        print('Todos:')
        for todo_id in todos:
            print(f'{todo_id.decode()} - {self.r.get(todo_id).decode()}')

    def update_todo(self, todo_id, new_text):
        if self.r.exists(todo_id):
            self.r.set(todo_id, new_text)
            print(f'Todo actualizado: {todo_id} - {new_text}')
        else:
            print(f'Error: No existe el TODO con ID {todo_id}')

    def delete_todo(self, todo_id):
        if self.r.exists(todo_id):
            self.r.delete(todo_id)
            print(f'Todo eliminado: {todo_id}')
        else:
            print(f'Error: No existe el TODO con ID {todo_id}')

def main():
    todo_crud = TodoCRUD()

    while True:
        print("\n----- Menú Principal -----")
        print("1. Crear Todo")
        print("2. Leer Todos")
        print("3. Actualizar Todo")
        print("4. Eliminar Todo")
        print("5. Salir")

        choice = input("Seleccione una opción (1-5): ")

        if choice == '1':
            todo_id = input("Ingrese el ID del Todo: ")
            todo_text = input("Ingrese el texto del Todo: ")
            todo_crud.create_todo(todo_id, todo_text)

        elif choice == '2':
            todo_crud.read_all_todos()

        elif choice == '3':
            todo_id = input("Ingrese el ID del Todo que desea actualizar: ")
            new_text = input("Ingrese el nuevo texto del Todo: ")
            todo_crud.update_todo(todo_id, new_text)

        elif choice == '4':
            todo_id = input("Ingrese el ID del Todo que desea eliminar: ")
            todo_crud.delete_todo(todo_id)

        elif choice == '5':
            print("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
