class FilterModule(object):
    def filters(self):
        return {'ans_filter': self.ans_filter}

    def ans_filter(self, play_variable):
        ans_new_variable = play_variable + ' VISHNU!!!!!!!!!!!!'
        return ans_new_variable
