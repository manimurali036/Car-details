# Simulated transformer model behavior for demonstration
# No external APIs or requests used

# Predefined sample data (as if a transformer predicted it)
sample_data = {
    "toyota": [
        {"Model_Name": "Camry"},
        {"Model_Name": "Corolla"},
        {"Model_Name": "RAV4"},
        {"Model_Name": "Prius"},
        {"Model_Name": "Highlander"},
        {"Model_Name": "Tacoma"},
        {"Model_Name": "Tundra"},
        {"Model_Name": "4Runner"},
        {"Model_Name": "Avalon"},
        {"Model_Name": "Yaris"}
    ],
    "honda": [
        {"Model_Name": "Civic"},
        {"Model_Name": "Accord"},
        {"Model_Name": "CR-V"},
        {"Model_Name": "Pilot"},
        {"Model_Name": "Odyssey"},
        {"Model_Name": "Fit"},
        {"Model_Name": "Ridgeline"},
        {"Model_Name": "HR-V"},
        {"Model_Name": "Passport"},
        {"Model_Name": "Insight"}
    ]
}

# Simulated vehicle specs
specs_data = {
    "Camry": ["Passenger Car", "Sedan"],
    "Corolla": ["Passenger Car", "Compact"],
    "RAV4": ["Multipurpose Passenger Vehicle", "SUV"],
    "Civic": ["Passenger Car", "Compact"],
    "Accord": ["Passenger Car", "Sedan"],
    "CR-V": ["SUV", "Crossover"],
}

def get_models_by_make(make):
    return sample_data.get(make.lower(), [])

def get_vehicle_specification(make, model):
    return specs_data.get(model, [])

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
                for s in specs:
                    print(f"- Vehicle Type: {s}")
            else:
                print("No specifications found.")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
