# User Stories

---
#### Every user story answers:
- Business Question
- Descriptive Analysis
- Statistical Validation
- Executive Recommendation

# User Story 1: Discount Strategy Analysis

## Business Problem

Management suspects that aggressive discounting increases sales but may be reducing overall profitability.

## User Story

As a Sales Director, I want to understand how discount levels impact profitability so that I can identify discount practices that reduce company earnings.

## Acceptance Criteria

### Business Analysis
- [ ] Discount percentages are grouped into meaningful bands.
- [ ] Average sales are calculated for each discount band.
- [ ] Average profit is calculated for each discount band.
- [ ] Loss-making products are identified.
- [ ] Dashboard highlights profitability deterioration thresholds.

### Statistical Validation
- [ ] Correlation between discount and profit is calculated.
- [ ] Statistical significance of the relationship is tested.
- [ ] Confidence intervals for average profit are reported.
- [ ] Results include p-values and business interpretation.

## Tasks

### Data Analysis
- [ ] Calculate profit by discount band.
- [ ] Calculate sales by discount band.
- [ ] Calculate average discount per product.
- [ ] Identify loss-making products.

### Statistical Analysis
- [ ] Perform Pearson correlation between Discount and Profit.
- [ ] Perform Spearman correlation as a robustness check.
- [ ] Divide observations into discount groups.
- [ ] Conduct two-sample t-test.
- [ ] Calculate 95% confidence intervals for average profit.

### Visualisation
- [ ] Discount vs Profit scatter plot.
- [ ] Profit by Discount Band chart.
- [ ] Correlation heatmap.
- [ ] Loss-making products chart.

### Dashboard
- [ ] Discount Analysis section.
- [ ] Average Discount KPI.
- [ ] Total Profit KPI.
- [ ] Loss-Making Orders KPI.
- [ ] Statistical Significance KPI.

### Executive Insight
- [ ] Recommend optimal discount policy.
- [ ] Identify discount levels associated with lower profitability.

---

# User Story 2: Regional Performance Analysis

## Business Problem

Some regions generate strong sales but low profit.

## User Story

As a Regional Manager, I want to compare sales and profitability across regions so that I can identify underperforming markets and improve resource allocation.

## Acceptance Criteria

### Business Analysis
- [ ] Sales are reported by region.
- [ ] Profit is reported by region.
- [ ] Profit margin is calculated.
- [ ] Loss-making regions are highlighted.
- [ ] Regional rankings are provided.

### Statistical Validation
- [ ] Profit differences across regions are tested.
- [ ] ANOVA results are reported.
- [ ] Post-hoc tests identify specific regional differences.
- [ ] Confidence intervals are provided.

## Tasks

### Data Analysis
- [ ] Aggregate sales by region.
- [ ] Aggregate profit by region.
- [ ] Compute profit margins.
- [ ] Rank regions by performance.

### Statistical Analysis
- [ ] Perform one-way ANOVA on regional profits.
- [ ] Perform Tukey HSD post-hoc test.
- [ ] Calculate 95% confidence intervals by region.

### Visualisation
- [ ] Sales by Region chart.
- [ ] Profit by Region chart.
- [ ] Profit Margin chart.
- [ ] Regional comparison dashboard.

### Dashboard
- [ ] Regional KPI section.
- [ ] Region ranking table.
- [ ] Best-performing region highlight.
- [ ] Worst-performing region highlight.

### Executive Insight
- [ ] Identify strongest regions.
- [ ] Identify weakest regions.
- [ ] Recommend opportunities for regional improvement.

---

# User Story 3: Product Portfolio Analysis

## Business Problem

Not all products contribute equally to profitability.

## User Story

As a Product Portfolio Manager, I want to identify which product categories generate the highest profits so that I can prioritise investment in profitable products and reduce losses from underperforming categories.

## Acceptance Criteria

### Business Analysis
- [ ] Sales are reported for all categories.
- [ ] Profit is reported for all categories.
- [ ] Top-performing categories are identified.
- [ ] Bottom-performing categories are identified.
- [ ] Contribution to overall profit is calculated.

### Statistical Validation
- [ ] Profit differences among categories are tested.
- [ ] ANOVA results are reported.
- [ ] Confidence intervals are reported.

## Tasks

### Data Analysis
- [ ] Aggregate sales by category.
- [ ] Aggregate profit by category.
- [ ] Aggregate profit by sub-category.
- [ ] Calculate contribution to total profit.

### Statistical Analysis
- [ ] Perform ANOVA across product categories.
- [ ] Calculate confidence intervals for category profit.

### Visualisation
- [ ] Sales by Category chart.
- [ ] Profit by Category chart.
- [ ] Profit Contribution chart.
- [ ] Top and Bottom Sub-category chart.

### Dashboard
- [ ] Product Performance section.
- [ ] Top 10 Products table.
- [ ] Bottom 10 Products table.

### Executive Insight
- [ ] Identify profit drivers.
- [ ] Identify loss leaders.
- [ ] Recommend investment priorities.

---

# User Story 4: Customer Segment Analysis

## Business Problem

Different customer segments contribute differently to revenue and profit.

## User Story

As a Marketing Manager, I want to analyse profitability by customer segment so that I can focus marketing efforts on the most valuable customer groups.

## Acceptance Criteria

### Business Analysis
- [ ] Sales are reported by customer segment.
- [ ] Profit is reported by customer segment.
- [ ] Segment rankings are provided.
- [ ] Average order value is calculated.

### Advanced Analytics
- [ ] Customer segments are analysed using K-Means clustering.
- [ ] High-value customer groups are identified.
- [ ] Cluster profiles are documented.

## Tasks

### Data Analysis
- [ ] Aggregate sales by segment.
- [ ] Aggregate profit by segment.
- [ ] Calculate average order value.
- [ ] Calculate customer frequency metrics.

### Machine Learning
- [ ] Scale customer features.
- [ ] Apply K-Means clustering.
- [ ] Determine optimal number of clusters.
- [ ] Profile customer clusters.

### Visualisation
- [ ] Profit by Segment chart.
- [ ] Sales by Segment chart.
- [ ] Cluster visualisation.
- [ ] Customer value dashboard.

### Dashboard
- [ ] Customer Segment section.
- [ ] Revenue KPI.
- [ ] Profit KPI.
- [ ] Orders KPI.

### Executive Insight
- [ ] Identify high-value customers.
- [ ] Recommend customer targeting strategies.

---

# User Story 5: Shipping Mode Analysis

## Business Problem

Delivery choices may be reducing profit through excessive shipping costs.

## User Story

As an Operations Manager, I want to evaluate the profitability of different shipping modes so that I can balance customer service levels with operational costs.

## Acceptance Criteria

### Business Analysis
- [ ] Sales are reported by shipping mode.
- [ ] Profit is reported by shipping mode.
- [ ] Shipping methods are ranked.
- [ ] Profitability differences are identified.

### Statistical Validation
- [ ] Profit differences between shipping modes are tested.
- [ ] ANOVA results are reported.
- [ ] Confidence intervals are provided.

## Tasks

### Data Analysis
- [ ] Aggregate sales by shipping mode.
- [ ] Aggregate profit by shipping mode.
- [ ] Calculate average profit per order.

### Statistical Analysis
- [ ] Perform ANOVA across shipping modes.
- [ ] Perform Tukey HSD post-hoc testing.
- [ ] Calculate confidence intervals.

### Visualisation
- [ ] Profit by Ship Mode chart.
- [ ] Sales by Ship Mode chart.
- [ ] Order Count by Ship Mode chart.

### Dashboard
- [ ] Shipping Insight section.
- [ ] Shipping KPI cards.
- [ ] Best shipping mode highlight.
- [ ] Least profitable shipping mode highlight.

### Executive Insight
- [ ] Recommend cost-effective shipping methods.
- [ ] Highlight operational improvement opportunities.

---

# User Story 6: Profit Prediction

## Business Problem

Management wants to identify key drivers of profitability and predict future performance.

## User Story

As an Executive Stakeholder, I want a predictive model that estimates profit so that I can make data-driven strategic decisions.

## Acceptance Criteria

- [ ] Predictive model is developed.
- [ ] Model performance is evaluated.
- [ ] Important features are identified.
- [ ] Results are visualised.

## Tasks

### Machine Learning
- [ ] Build Linear Regression model.
- [ ] Build Random Forest Regressor.
- [ ] Compare model performance.

### Evaluation
- [ ] Calculate MAE.
- [ ] Calculate RMSE.
- [ ] Calculate R².

### Explainability
- [ ] Compute feature importance.
- [ ] Rank profitability drivers.

### Executive Insight
- [ ] Identify factors with greatest influence on profit.
- [ ] Recommend actions based on model findings.

---

# User Story 7: Profitability Classification

## Business Problem

Management wants to identify orders that are likely to become loss-making.

## User Story

As a Risk-Aware Decision Maker, I want to classify transactions as profitable or unprofitable so that I can minimise future losses.

## Acceptance Criteria

- [ ] Orders are classified as profit or loss.
- [ ] Model performance is evaluated.
- [ ] Classification metrics are reported.

## Tasks

### Machine Learning
- [ ] Create target variable (Profitable vs Unprofitable).
- [ ] Train Logistic Regression model.

### Evaluation
- [ ] Generate Confusion Matrix.
- [ ] Calculate Accuracy.
- [ ] Calculate Precision.
- [ ] Calculate Recall.
- [ ] Calculate F1 Score.

### Executive Insight
- [ ] Identify risk factors associated with loss-making transactions.
- [ ] Recommend mitigation strategies.