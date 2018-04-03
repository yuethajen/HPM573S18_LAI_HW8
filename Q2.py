import Classes as Cls
import SupportTransientState as Support

# create multiple games head_prob=0.5
multiGames1 = Cls.MultipleGameSets(
    ids=range(1000),
    prob_head=0.5,
    n_games_in_a_set=10
)

# simulate all games
multiGames1.simulation()

# create multiple games head_prob=0.45
multiGames2 = Cls.MultipleGameSets(
    ids=range(1000),
    prob_head=0.45,
    n_games_in_a_set=10
)

# simulate all games
multiGames2.simulation()

# print outcomes of each cohort
Support.print_outcomes(multiGames1, 'Head probability = 0.5:')
print('')
Support.print_outcomes(multiGames2, 'Head probability = 0.45:')
print('')

# draw histograms of average survival time
Support.draw_histograms(multiGames1, multiGames2)

# print comparative outcomes
Support.print_comparative_outcomes(multiGames1, multiGames2)
