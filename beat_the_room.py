import time
from threading import Thread
import Puzzle1

class Controller(object):
    def __init__(self):
        puz1 = Puzzle1.Puzzle1(self)
        self.puzzles = [puz1]
        self.active_puzzles = []

        self.hint_queue = []

        self.run_thread = Thread(target=self.run)
        self.run_thread.start()

    def run(self):
        print('running')
        self.activate(self.puzzles[0].id)
        print(self.puzzles)
        pass

    def reset_timer(self):
        pass

    def deactivate(self, puzzle): # muss hinweis und puzzle entfernen
        self.active_puzzles.pop(self.active_puzzles.index(puzzle))
        puzzle.activated = False
        #vllt zu puzzles hinzufügen

        for hint in puzzle.hints:
            hint_queue.pop(hint_queue.index(hint))
        pass

    def activate(self, id):
        for x in self.puzzles:
            if x.id == id:
                x.activated = True
                #vllt aus puzzles löschen
                break
        pass

class Puzzle(object):
    def __init__(self, controller):
        self.id = None
        self.controller = controller

        self.hints = []

        self.activates_ids = []

        self.activated = False
        self.solved = False

        self.run_thread = Thread(target=self.run_thread_func)
        self.run_thread.start()

        self.interact_thread = Thread(target=self.interact)

    def run_thread_func(self):
        self.init()

        while not self.activated:
            pass

        self.controller.active_puzzles.append(self)
        self.interact_thread.start()

        while not self.solved:
            pass

        self.controller.reset_timer()
        self.controller.deactivate(self)
        for id in self.activates_ids:
            self.controller.activate(id)

        self.deinit()

    def init(self):
        raise NotImplementedError

    def interact(self):
        raise NotImplementedError

    def deinit(self):
        raise NotImplementedError


class Hint(object):
    def __init__(self, puzzle, file):
        self.puzzle = puzzle
        self.file = file
if __name__ == '__main__':
    print('Hi')
    c = Controller()
