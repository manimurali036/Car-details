import requests

def get_models_by_make(make):
    url = f"https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/{make}?format=json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        models = data.get('Results', [])
        return models
    else:
        print("Failed to fetch model data.")
        return []

def get_vehicle_specification(make, model):
    url = f"https://vpic.nhtsa.dot.gov/api/vehicles/GetVehicleTypesForMakeModel/{make}/{model}?format=json"
    response = requests.get(url)

    if response.status_code == 200:
        specs = response.json().get('Results', [])
        return specs
    else:
        print("Failed to fetch specifications.")
        return []

def main():
    make = input("Enter car make (e.g., Toyota, Honda): ").lower()
    models = get_models_by_make(make)

    if not models:
        print("No models found.")
        return

    print(f"\nFound {len(models)} models for '{make.title()}':")
    for idx, model in enumerate(models[:10]):
        print(f"{idx + 1}. {model['Model_Name']}")

    try:
        choice = int(input("\nSelect a model number for specifications (1-10): ")) - 1
        if 0 <= choice < len(models[:10]):
            selected_model = models[choice]['Model_Name']
            print(f"\nFetching specifications for: {make.title()} {selected_model}...")
            specs = get_vehicle_specification(make, selected_model)
            if specs:
                print("\nVehicle Types / Specifications:")
                for spec in specs:
                    print(f"- Vehicle Type: {spec['VehicleTypeName']}")
            else:
                print("No specifications found.")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
