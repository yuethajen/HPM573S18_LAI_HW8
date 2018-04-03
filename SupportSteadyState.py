import scr.FormatFunctions as Format
import scr.FigureSupport as Figs
import scr.StatisticalClasses as Stat


def print_outcomes(sim_output, strategy_name):
    """ prints the outcomes of a simulated cohort under steady state
    :param sim_output: output of a simulated cohort
    :param strategy_name: the name of the selected therapy
    """

    # mean and confidence interval text of rewards
    survival_mean_CI_text = Format.format_estimate_interval(
        estimate=sim_output.get_ave_reward(),
        interval=sim_output.get_CI_reward(alpha=0.05),
        deci=1)

    # print rewards statistics
    print(strategy_name)
    print("Estimate of mean expected reward ($) and {:.{prec}%} confidence interval:".format(1 - 0.05, prec=0),
          survival_mean_CI_text)


def draw_survival_curves_and_histograms(sim_output_1, sim_output_2):
    """ draws the survival curves and the histograms of survival time
    :param sim_output_no_drug: output of a cohort simulated when drug is not available
    :param sim_output_with_drug: output of a cohort simulated when drug is available
    """

    # histograms of rewards
    set_of_rewards = [
        sim_output_1.get_rewards(),
        sim_output_2.get_rewards()
    ]

    # graph histograms
    Figs.graph_histograms(
        data_sets=set_of_rewards,
        title='Histogram of rewards',
        x_label='Rewards',
        y_label='Counts',
        bin_width=15,
        legend=['50%', '45%'],
        transparency=0.6
    )


def print_comparative_outcomes(sim_output_1, sim_output_2):
    """ prints expected and percentage increase in survival time when drug is available
    :param sim_output_no_drug: output of a cohort simulated when drug is not available
    :param sim_output_with_drug: output of a cohort simulated when drug is available
    """

    # increase in survival time
    increase = Stat.DifferenceStatIndp(
        name='Increase in rewards',
        x=sim_output_2.get_rewards(),
        y_ref=sim_output_1.get_rewards()
    )
    # estimate and CI
    estimate_CI = Format.format_estimate_interval(
        estimate=increase.get_mean(),
        interval=increase.get_t_CI(alpha=0.05),
        deci=1
    )
    print("Average increase in rewards ($) and {:.{prec}%} confidence interval:".format(1 - 0.05, prec=0),
          estimate_CI)

