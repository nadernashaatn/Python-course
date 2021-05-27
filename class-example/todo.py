class Todo:
    
    """
    Implement the Todo Class
    """

    def __init__(self, name, description, points, completed=False):
       self.name = name
       self.description = description
       self.points = points
       self.completed = completed

    def __repr__(self):
        return (f" Task Name: {self.name} \n Task status: {self.completed} \n Task points: {self.points}")  


class TodoList:

    def __init__(self, todos):
        self.todos = todos

    def averge_points(self):
        total = 0 
        for todo in self.todos:
            total += todo.points
        return total / len(self.todos)


