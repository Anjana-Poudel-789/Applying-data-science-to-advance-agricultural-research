# Potato Dormancy Breaking Treatments Analysis

This repository contains code and results from an analysis of different chemical treatments for breaking potato dormancy. The study compares the effectiveness of Water (control), Gibberellic Acid (GA3), Thiourea, and Indole Acetic Acid (IAA) in promoting potato tubesr sprouting.

## Research Background

Potato tubers naturally undergo a period of dormancy after harvest, during which they won't sprout even under favorable conditions. Breaking this dormancy is crucial for optimizing planting schedules and ensuring uniform crop emergence. This study investigates the effectiveness of different chemical treatments in accelerating the sprouting process.

## Methodology

Four treatments were applied to potato tubers:
- Water (control)
- Gibberellic Acid (GA3)
- Thiourea
- Indole Acetic Acid (IAA)

Sprouting was measured at three time points: 9, 17, and 28 days after treatment (DAT). The number of sprouted tubers was recorded for each treatment at each time point.

## Key Findings

- GA3 showed the highest effectiveness (93.2% improvement vs control)
- Thiourea and IAA showed moderate effectiveness (20% improvement)
- GA3 treatment reached 80% sprouting earlier than other treatments
- Results demonstrate GA3's potential for optimizing potato planting schedules

## Files Description

- `python_result_code.py`: Python script for data analysis and visualization
- `'Results Figure.png`: Figure showing the comprehensive analysis results
- `requirements.txt`: Required Python packages to run the analysis
# Limitations

- This analysis is based on single observations per treatment
- Future studies should include multiple replicates for statistical testing
- More time points would provide better understanding of treatment dynamics

## Figure Interpretation

The generated figure contains four panels:
1. **Top Left**: Bar chart comparing sprouted tubers at 17 DAT across treatments
2. **Top Right**: Line plot showing treatment effects over time
3. **Bottom Left**: Grouped bar chart showing treatment effects at different time points
4. **Bottom Right**: Treatment effectiveness comparison with percentage improvements

Significance letters (a, b) indicate visual differences between treatments, with different letters representing potentially meaningful differences.

# requirements.txt
pandas
matplotlib
numpy
scipy
seaborn

## Contact
Anjana Poudel
poudelanjana2057@gmail.com
Agriculture and Forestry University,Nepal



# Methods for Potato Dormancy Breaking Analysis

## Experimental Design

This experiment was designed to evaluate the effectiveness of different chemical treatments in breaking dormancy of potato tubers. The study employed a completely randomized design with four treatments and three measurement time points.

## Treatments

The following treatments were applied to potato tubers:

1. **Water (Control)**: Distilled water application(10 liters)
2. **Gibberellic Acid (GA3)**: 50 ppm solution of GA3
3. **Thiourea**: 1% solution of Thiourea
4. **Indole Acetic Acid (IAA)**: 40 ppm solution of IAA

## Application Method
A calculated amount of plant growth regulators (PGRs) was dissolved in water in separate plastic buckets to prepare the treatment solutions, targeting concentrations of 50 ppm for gibberellic acid (GA₃), 40 ppm for indole-3-acetic acid (IAA), 1% for thiourea, and clean water for the control. Specifically, 0.5 grams of GA₃ was dissolved in 10 liters of water, 12.5 grams of IAA was dissolved in 12.5 liters of water, and 50 grams of thiourea was dissolved in 5 liters of water. For the control, 10 liters of clean water was used. 


## Data Collection

Sprouting was assessed at three time points:
- 9 days after treatment (DAT)
- 17 days after treatment (DAT)
- 28 days after treatment (DAT)

At each assessment, the number of sprouted tubers was recorded for each treatment. A tuber was considered sprouted when the first sprout reached 2 mm in length.
## Data Analysis

Data analysis was performed using Python with the following libraries:
- pandas for data manipulation
- matplotlib and seaborn for visualization
- numpy and scipy for numerical operations

The analysis included:
1. Descriptive statistics of sprouting rates
2. Comparative visualization of treatment effects
3. Calculation of percentage improvement relative to control
4. Time-course analysis of sprouting dynamics

## Statistical Considerations

Due to the single observation per treatment at each time point, formal statistical testing (e.g., ANOVA) was not performed. Differences between treatments were evaluated through descriptive statistics and visual comparison. Future studies should incorporate multiple replicates to enable proper statistical analysis.

**Note**: This code and analysis represent a portion of ongoing research that has not yet been published. While shared for transparency and reproducibility, please do not copy or use this work without permission. If you're interested in building upon this research, please contact me to discuss collaboration opportunities.
