import Classes as Cls
import SupportSteadyState as Support


# expected rewards from 1000 games
setOfGames1 = Cls.SetOfGames(id=1, prob_head=0.5, n_games=1000)
setOfGames2 = Cls.SetOfGames(id=1, prob_head=0.45, n_games=1000)
outcomes1 = setOfGames1.simulation()
outcomes2 = setOfGames2.simulation()
setOfGamesOutcomes1 = Cls.SetOfGamesOutcomes(setOfGames1)
setOfGamesOutcomes2 = Cls.SetOfGamesOutcomes(setOfGames2)


# print outcomes
Support.print_outcomes(setOfGamesOutcomes1, 'Head probability = 0.5:')
print('')
Support.print_outcomes(setOfGamesOutcomes2, 'Head probability = 0.45:')
print('')

# draw survival curves and histograms
Support.draw_survival_curves_and_histograms(setOfGamesOutcomes1, setOfGamesOutcomes2)

# print comparative outcomes
Support.print_comparative_outcomes(setOfGamesOutcomes1, setOfGamesOutcomes2)
