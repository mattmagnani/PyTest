import pandas as pd

def calculate_ekranoplan_costs(wingspan_ft=55, material_quality='standard'):
    """
    Calculate estimated costs for ekranoplan components based on wingspan
    Args:
        wingspan_ft (float): Wingspan in feet
        material_quality (str): Quality level of materials ('standard', 'premium')
    Returns:
        DataFrame with cost breakdown and dictionary with summary statistics
    """
    # Base multipliers for material quality
    multiplier = 1.5 if material_quality == 'premium' else 1.0
    
    # Approximate surface area and volume calculations
    wing_area = wingspan_ft * (wingspan_ft / 3)  # Rough estimation
    hull_length = wingspan_ft * 1.2  # Typical ratio
    
    # Component costs (in USD)
    costs = {
        'Structural Components': {
            'Hull/Fuselage': {
                'Main hull structure': 75000 * multiplier,
                'Internal framing': 35000 * multiplier,
                'Water-tight compartments': 25000 * multiplier,
                'Surface treatment & coatings': 15000 * multiplier
            },
            'Wings': {
                'Wing structure': 45000 * multiplier,
                'Control surfaces': 30000 * multiplier,
                'Wing endplates': 20000 * multiplier,
                'PAR system integration': 35000 * multiplier
            }
        },
        'Propulsion': {
            'Main engines': {
                'Turboprop/turbofan engines': 180000 * multiplier,
                'Engine mounts': 15000 * multiplier,
                'Fuel system': 25000 * multiplier,
                'Cooling system': 12000 * multiplier
            },
            'Auxiliary systems': {
                'Lift engines': 85000 * multiplier,
                'Propellers': 25000 * multiplier,
                'Engine controls': 30000 * multiplier
            }
        },
        'Control Systems': {
            'Flight controls': {
                'Control surfaces actuators': 40000 * multiplier,
                'Hydraulic systems': 35000 * multiplier,
                'Control electronics': 45000 * multiplier
            },
            'Navigation': {
                'Avionics': 65000 * multiplier,
                'Sensors': 35000 * multiplier,
                'Navigation systems': 40000 * multiplier
            }
        },
        'Landing Systems': {
            'Water operations': {
                'Hull reinforcement': 25000 * multiplier,
                'Water skids/skis': 15000 * multiplier,
                'Shock absorption': 20000 * multiplier
            },
            'Landing gear': {
                'Retractable gear': 35000 * multiplier,
                'Hydraulics': 25000 * multiplier,
                'Controls': 15000 * multiplier
            }
        },
        'Interior & Safety': {
            'Cabin': {
                'Interior structure': 30000 * multiplier,
                'Climate control': 20000 * multiplier,
                'Seating & restraints': 25000 * multiplier
            },
            'Safety equipment': {
                'Life rafts': 15000 * multiplier,
                'Fire suppression': 12000 * multiplier,
                'Emergency equipment': 18000 * multiplier
            }
        },
        'Labor & Assembly': {
            'Engineering': 150000,
            'Assembly': 120000,
            'Testing': 80000,
            'Certification': 60000
        }
    }
    
    # Convert nested dictionary to flat DataFrame
    rows = []
    for category, subcategories in costs.items():
        for subcategory, items in subcategories.items():
            for item, cost in items.items():
                rows.append({
                    'Category': category,
                    'Subcategory': subcategory,
                    'Item': item,
                    'Cost': cost
                })
    
    df = pd.DataFrame(rows)
    
    # Calculate summary statistics
    summary = {
        'total_cost': df['Cost'].sum(),
        'highest_category': df.groupby('Category')['Cost'].sum().idxmax(),
        'highest_cost_item': df.loc[df['Cost'].idxmax(), 'Item'],
        'cost_per_ft_wingspan': df['Cost'].sum() / wingspan_ft,
        'structural_percentage': df[df['Category'] == 'Structural Components']['Cost'].sum() / df['Cost'].sum() * 100,
        'propulsion_percentage': df[df['Category'] == 'Propulsion']['Cost'].sum() / df['Cost'].sum() * 100
    }
    
    return df, summary

# Example usage
df, summary = calculate_ekranoplan_costs(wingspan_ft=55, material_quality='standard')