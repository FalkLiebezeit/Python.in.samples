"""Interactive HTML Charts with Plotly

This module demonstrates how to create interactive visualizations using Plotly.
The charts are interactive and can be exported as standalone HTML files.
"""

import plotly.express as px
import pandas as pd


def create_sample_data() -> pd.DataFrame:
    """Generate sample data for visualization.
    
    Returns:
        DataFrame with X and Y values for plotting
    """
    return pd.DataFrame({
        "X-Values": [1, 2, 3, 4, 5],
        "Y-Values": [10, 20, 15, 30, 25]
    })


def create_line_chart(data: pd.DataFrame, x_col: str, y_col: str, title: str) -> None:
    """Create and display an interactive line chart.
    
    Args:
        data: DataFrame containing the data to plot
        x_col: Name of the column for x-axis
        y_col: Name of the column for y-axis
        title: Chart title
        
    Features:
        - Interactive zoom and pan
        - Hover tooltips showing data points
        - Export to PNG capability
        - Responsive layout
    """
    fig = px.line(
        data, 
        x=x_col, 
        y=y_col, 
        title=title,
        markers=True,
        template="plotly_white"  # Clean, professional theme
    )
    
    # Customize layout for better appearance
    fig.update_layout(
        xaxis_title=x_col,
        yaxis_title=y_col,
        hovermode='x unified',  # Better hover interaction
        font=dict(size=12)
    )
    
    # Enhance marker appearance
    fig.update_traces(
        marker=dict(size=8, line=dict(width=2, color='white')),
        line=dict(width=3)
    )
    
    # Display the chart (opens in browser)
    fig.show()
    
    # Optionally save to HTML file
    # fig.write_html("interactive_chart.html")


def main():
    """Main function to demonstrate interactive chart creation."""
    # Create sample dataset
    data = create_sample_data()
    
    # Generate and display interactive line chart
    create_line_chart(
        data=data,
        x_col="X-Values",
        y_col="Y-Values",
        title="Interactive Line Chart with Plotly"
    )


if __name__ == "__main__":
    main()