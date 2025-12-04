enum Priority {
    LOW = 0,
    MEDIUM = 1,
    HIGH = 2
}

interface Task {
    id:number,
    title:string,
    completed:boolean,
    priority:Priority
}

class TaskManager {
    private tasks:Task[];
    private nextId:number;
    constructor() {
        this.tasks = [];
        this.nextId = 1;
    }

    addTask(title:string, priority: Priority | null = null): Task{
        const tempVar: Task = {
            id: this.nextId++,
            title: title,
            completed: false,
            priority: priority ?? Priority.LOW
        }
        this.tasks.push(tempVar);
        return tempVar;
    }

    completeTask(id:number): boolean{
        const task = this.tasks.find(x => x.id === id);
        if(!task){
            return false;
        }
        task.completed = true;
        return true;
    }

    getTasksByPriority(priority: Priority): Task[]{
        return this.tasks.filter(task => task.priority === priority);
    }

    getPendingTasksCount(): number {
        return this.tasks.filter(task => !task.completed).length;
    }

    removeTask(id: number): boolean {
        const index = this.tasks.findIndex(task => task.id === id);

        if (index === -1) {
            return false; // nincs ilyen feladat
        }

        this.tasks.splice(index, 1); // törlés
        return true;
    }

    updateTaskPriority(id: number, newPriority: Priority): boolean {
        const task = this.tasks.find(t => t.id === id);
        if (!task) {
            return false;
        }
        task.priority = newPriority;
        return true;
    }

}