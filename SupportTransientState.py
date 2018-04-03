import scr.FormatFunctions as Format
import scr.FigureSupport as Figs
import scr.StatisticalClasses as Stat


def print_outcomes(multi_cohort, strategy_name):
    """ prints the outcomes of a simulated cohort under steady state
    :param multi_cohort: output of a simulated cohort
    :param strategy_name: the name of the selected therapy
    """

    # mean and confidence interval text of rewards
    survival_mean_PI_text = Format.format_estimate_interval(
        estimate=multi_cohort.get_mean_total_reward(),
        interval=multi_cohort.get_PI_total_reward(alpha=0.05),
        deci=1)

    # print reward statistics
    print(strategy_name)
    print("Estimate of mean rewards ($) and {:.{prec}%} prediction interval:".format(1 - 0.05, prec=0),
          survival_mean_PI_text)


def draw_histograms(multiGames1, multiGames2):

    # histograms of average rewards
    set_of_rewards = [
        multiGames1.get_all_total_rewards(),
        multiGames2.get_all_total_rewards()
    ]

    # graph histograms
    Figs.graph_histograms(
        data_sets=set_of_rewards,
        title='Histogram of total rewards (in 10 games)',
        x_label='Rewards',
        y_label='Counts',
        bin_width=15,
        legend=['50%', '45%'],
        transparency=0.5,
        x_range=[-1500, 1000]
    )


def print_comparative_outcomes(multiGames1, multiGames2):

    # increase in rewards
    increase = Stat.DifferenceStatIndp(
        name='Increase in rewards',
        x=multiGames2.get_all_total_rewards(),
        y_ref=multiGames1.get_all_total_rewards()
    )

    # estimate and prediction interval
    estimate_CI = Format.format_estimate_interval(
        estimate=increase.get_mean(),
        interval=increase.get_PI(alpha=0.05),
        deci=1
    )
    print("Expected increase in total rewards ($) and {:.{prec}%} prediction interval:".format(1 - 0.05, prec=0),
          estimate_CI)



