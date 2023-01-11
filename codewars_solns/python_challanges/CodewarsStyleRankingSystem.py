class User:
    progress_list=[ -8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8]
    def __init__(self):
        """initialising instance variables"""
        self.rank = -8
        self.progress = 0

    def inc_progress(self, q_rank):
        """method to track progress"""
        rank_contribution = 0
        if q_rank in User.progress_list:
            if not self.rank == 8:
                rank_index = User.progress_list.index(self.rank)
                q_rank_index = User.progress_list.index(q_rank)
                rank_index_max= User.progress_list.index(8)
                if q_rank_index == rank_index:
                    score_gain = 3
                    self.progress += score_gain
                elif q_rank_index == rank_index-1:
                    score_gain = 1
                    self.progress += score_gain
                elif q_rank_index <= rank_index-2:
                    score_gain = 0
                    self.progress += score_gain
                else:
                    ranking_difference = q_rank_index - rank_index
                    score_gain = 10 * ranking_difference ** 2
                    rank_contribution = score_gain//100
                    self.progress += score_gain-rank_contribution*100

                if rank_contribution == 0:
                    if self.progress >= 100:
                        self.progress -= 100
                        if self.rank < 8:
                            self.rank = User.progress_list[rank_index+1]
                            if self.rank == 8:
                                self.progress = 0
                else:
                    if self.progress >= 100:
                        self.progress -= 100
                        if rank_index+rank_contribution < rank_index_max:
                            self.rank = User.progress_list[rank_index+rank_contribution+1]
                        else:
                            self.rank = 8
                            self.progress = 0
                    else:
                        if rank_index+rank_contribution < rank_index_max:
                            self.rank = User.progress_list[rank_index+rank_contribution]
                        else:
                            self.rank = 8
                            self.progress = 0
        else:
            raise ValueError

