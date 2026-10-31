# DEPI-Graduation-Project
DEPI Graduation Project repository for project work, updates, documentation, and deliverables.
📊 Enterprise Resource Planning (ERP) Transformation & Adoption Analytics

📌 Project Overview

This capstone project provides an end-to-end, data-driven analytical assessment of Enterprise Resource Planning (ERP) implementations across enterprise organizations. By ingesting and modeling 11 consolidated relational datasets encompassing over 100,000 organization records, the solution evaluates financial performance gains, technical infrastructure scalability, operational efficiencies, vendor performance, and human capital change management.

The analytics engine is designed to answer critical executive business questions, ranging from Return on Investment (ROI) realization windows and Days Sales Outstanding (DSO) reductions to customization cost drivers, license waste identification, and supply chain fulfillment bottlenecks.

🎯 Key Business Objectives & Value Proposition

1-Financial Transformation & ROI Tracking:

Quantify ROI realization timelines (in months) across deployment models (Cloud vs. On-Premises).

Evaluate financial close cycle day reductions and post-implementation audit exception rates.

2-Implementation & Vendor Risk Management:

Pinpoint root causes for budget variances, implementation delays, and customization cost escalations.

Compare vendor/partner contract performance (Fixed Price vs. Time & Materials) against SLA compliance.

3-Operational & Supply Chain Optimization:

Analyze warehouse fulfillment lead times, inventory discrepancy rates, and stockout frequency.

Determine vendor on-time delivery rates across manufacturing and retail sectors.

4-Change Management & Governance:

Measure the impact of C-level sponsorship and user training hours on employee resistance levels.

Audit software license utilization to identify unutilized annual expenditure and compliance risks (SoD violations).

🏗 Data Architecture & Relational Structure

The project builds a unified Star Schema Relational Data Model inside Power BI and MS Excel, linked seamlessly via the primary key Company_ID.

                        +----------------------------+
                        |   Company_Adoption (Fact)  |
                        +----------------------------+
                                      |
         +----------------------------+----------------------------+
         |                            |                            |
+------------------+        +-------------------+        +--------------------+
| Outcomes_KPIs    |        | HR_Change         |        | Tech_Infrastructure|
+------------------+        +-------------------+        +--------------------+
| Finance_Trans.   |        | Problem_Modules   |        | Security_Audit     |
+------------------+        +-------------------+        +--------------------+
| Partners_Vendors |        | Project_Phases    |        | Supply_Chain       |
+------------------+        +-------------------+        +--------------------+
                                                         | User_Licenses      |
                                                         +--------------------+


📁 Consolidated Datasets Summary

1-Company_Adoption: Organization baseline, industry sector, primary ERP system, deployment type.

2-Outcomes_KPIs: ROI realization months, post-go-live satisfaction score, process efficiency gains.

3-HR_Change: Training hours per employee, resistance rating, helpdesk ticket volumes.

4-Finance_Transformation: Financial close cycle reduction days, DSO reduction, invoice cost savings.

5-Partners_Vendors: Implementation partner, contract type, dispute rates, SLA compliance scores.

6-Problem_Modules: Specific module failure rates (Finance, SCM, HR, Manufacturing) and delay causes.

7-Project_Phases: Phase durations, planned vs. actual milestone timelines, budget overruns.

8-Security_Audit: SoD violations, data breach incidents, 2FA enforcement, patch frequency.

9-Supply_Chain: Order fulfillment hours, inventory discrepancy rates, vendor delivery rates.

10-Tech_Infrastructure: Database engines, cloud providers, migration volume, go-live downtime.

11-User_Licenses: Total licenses purchased, active users, unutilized annual license expense.

🛠 Technology Stack & Execution Tracks

The project employs a Dual-Track Parallel Execution Architecture to deliver high-impact analytics across two industry-standard platforms:

🔹 Track A: Power BI Analytics Stack

ETL & Data Cleaning: Power Query M-Engine for automated data cleaning, null handling, and type enforcement.

Data Modeling: Star Schema star-flake architecture with explicit 1-to-Many single-direction filtering relationships.

DAX Calculation Engine: Custom explicit measures for time intelligence, dynamic KPI ratios, and aggregate performance.

UI/UX Visual Layer: Interactive multi-tab executive dashboard featuring dynamic slicers, bookmark navigation, and drill-through tooltips.

🔹 Track B: MS Excel Analytics Stack

Data Auditing & Normalization: Direct data auditing and structured tabular transformations.

Master Dataset Consolidation: Unified multi-sheet workbook (All_ERP_Data.xlsx) linking all 11 tables.

Reporting Engine: Interactive PivotTables, PivotCharts, Slicers, and Timeline controls for standalone decision-making.

👥 Project Team & Track Responsibilities

Mahmoud Ali Mohamed Khallaf — Management & Media Lead: Project documentation, presentation decks, cross-track alignment, and media.

Malak Mahmoud Adawi — Excel Track Lead: Raw data auditing, cleaning, and structural normalization in Excel.

Asmaa Rabea Elshall — Excel Dashboard Lead: PivotTable logic, dynamic charts, and Excel UI Slicer layout design.

Mahmoud Ali Basuony — Power BI Modeling Lead: Power Query ETL, data schema architecture, and table relationship setup.

Mohamed Magdy Youssef — Power BI DAX Lead: Advanced DAX measures, time-intelligence calculations, and metric logic.

Ayat Tamer Mohamed Asar — Power BI UI/UX Lead: Executive visual design, color system, layout hierarchy, and user navigation.


📅 Project Roadmap & Timeline

Oct 20 ─── Oct 25 ─── Oct 30 ─── Nov 05 ─── Nov 10 ─── Nov 15 ─── Nov 25
  │          │          │          │          │          │          │
  ├──[P1]────┤          │          │          │          │          │  P1: PBI ETL & Modeling (Completed)
  ├───────[P2]──────────┤          │          │          │          │  P2: Excel Cleaning & Structuring (Completed)
  │          ├──────[P3]───────────┤          │          │          │  P3: PBI DAX Engine Development (Completed)
  │                     │          ├──[P4]────┤          │          │  P4: Excel Pivots & Dashboard (Nov 01-10)
  │                     │                     ├──[P5]────┤          │  P5: PBI Dashboard UI/UX Design (Nov 06-15)
  │                     │                                └────[P6]──┤  P6: Final Documentation & Video (Nov 16-25)


Phase 1 (Oct 20 – Oct 25) [Completed]: Power Query ETL & Star Schema Relational Modeling.

Phase 2 (Oct 20 – Oct 30) [Completed]: Excel Comprehensive Data Cleaning & Single Master File Assembly.

Phase 3 (Oct 26 – Nov 05) [Completed]: Core DAX Business Engine & Calculated Measures.

Phase 4 (Nov 01 – Nov 10) [Upcoming]: Excel Standalone Interactive Dashboard & Pivot Development.

Phase 5 (Nov 06 – Nov 15) [Upcoming]: Power BI Interactive Visual Layer & Page Design.

Phase 6 (Nov 16 – Nov 25) [Upcoming]: Cross-Track Reconciliation, Final Report, Presentation, and Video Demo.

📂 Repository Structure

├── Phase_1_Documentation/
│   ├── 1_Project_Planning_and_Management.pdf
│   ├── 2_Literature_Review.pdf
│   └── 3_Requirements_Gathering.pdf
├── Data/
│   ├── Raw_CSV_Files/              # 11 original raw dataset files
│   └── All_ERP_Data.xlsx           # Consolidated cleaned Excel master dataset
├── Power_BI/
│   └── ERP_Analytics_Model.pbix     # Power BI data model and DAX measures
├── Presentation/
│   └── ERP_Project_Phase1_Presentation.pdf
└── README.md


📜 License & Acknowledgments

This project is developed as part of the Digital Egypt Pioneers Initiative (DEPI) Capstone Program (2026). All data and findings are for educational and analytical benchmarking purposes.
