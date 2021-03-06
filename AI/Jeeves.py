from classes.transition_matrix import transition_matrix
class Jeeves:

    behavior_string = "Very cooperative; loathes competition"
    gender = "male"
    name = "Jeeves"
    matrix = transition_matrix(((1,0), (1,0)))

    def first_turn(self):
        return "cooperate"

    def take_turn(self, data=()):
        return self.matrix.get_decision(data)
