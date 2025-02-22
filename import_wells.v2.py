"""
PIPESIM Source Creation Script
Created: 2025-02-11 13:31:27 UTC
Author: wthesen
"""

from sixgill.pipesim import Model
from sixgill.definitions import ModelComponents, Parameters, Constants, CorrelationType
import pandas as pd
import numpy as np
import os

MODEL_PATH = r"C:\Program Files\Schlumberger\Pipesim2023.1\Hoole_Project\hoole_wells_2025-02-11 09-50-07.pips"

def create_sources():
    try:
        print(f"\nOpening existing model: {MODEL_PATH}")
        model = Model.open(MODEL_PATH)

        # Source definitions with their properties
        sources = [
            {
                "name": "Src-1",
                "lat": 56.08176078431267,
                "lon": -113.805337,
                "pressure": 1500,  # psia
                "temperature": 60,  # °F
                "gas_rate": 5000,  # Mscf/d
                "water_rate": 0,   # STB/d
                "oil_rate": 0      # STB/d
            },
            # Add more sources as needed with their properties
        ]

        print("\nCreating sources...")
        with model.batch_update():
            for src in sources:
                try:
                    source_name = src["name"]
                    print(f"\nCreating source: {source_name}")
                    
                    # Create the source
                    model.add(ModelComponents.SOURCE, source_name)
                    
                    # Set basic properties
                    model.set_value(context=source_name,
                                  parameter=Parameters.Location.LATITUDE,
                                  value=src["lat"])
                    
                    model.set_value(context=source_name,
                                  parameter=Parameters.Location.LONGITUDE,
                                  value=src["lon"])
                    
                    # Set source type to gas
                    model.set_value(context=source_name,
                                  parameter=Parameters.Source.TYPE,
                                  value="GAS")
                    
                    # Set operating conditions
                    model.set_value(context=source_name,
                                  parameter=Parameters.Source.PRESSURE,
                                  value=src["pressure"])
                    
                    model.set_value(context=source_name,
                                  parameter=Parameters.Source.TEMPERATURE,
                                  value=src["temperature"])
                    
                    # Set flow rates
                    model.set_value(context=source_name,
                                  parameter=Parameters.Source.GASRATE,
                                  value=src["gas_rate"])
                    
                    model.set_value(context=source_name,
                                  parameter=Parameters.Source.WATERRATE,
                                  value=src["water_rate"])
                    
                    model.set_value(context=source_name,
                                  parameter=Parameters.Source.OILRATE,
                                  value=src["oil_rate"])
                    
                    # Set correlation type (if needed)
                    model.set_value(context=source_name,
                                  parameter=Parameters.Source.CORRELATIONTYPE,
                                  value=CorrelationType.BEGGS_AND_BRILL)
                    
                    print(f"Successfully created {source_name}")
                    
                except Exception as e:
                    print(f"Error creating source {source_name}: {str(e)}")
                    import traceback
                    print(traceback.format_exc())

        print("\nSaving model...")
        model.save()
        
        # Optionally open in UI to verify
        model.open_ui()
        print("Operation complete - please verify sources in UI")

    except Exception as e:
        print(f"Error: {str(e)}")
        print(f"Error type: {type(e)}")
    finally:
        if 'model' in locals():
            try:
                model.close()
                print("Model closed successfully")
            except:
                pass

if __name__ == '__main__':
    create_sources()