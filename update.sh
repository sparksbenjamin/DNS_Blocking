set -e


#echo "Building services.json"
#python scripts/build_services.py

#echo "Running Services Script"
#python scripts/service_list_generator.py


#echo "Custom Cats"
#./scripts/build_categories.sh

echo "Run Generator"
python3 scripts/generator.py
echo "Running Quality Validation"
python3 scripts/validate_lists.py
echo "Running Tunneling Script"
python3 scripts/tunneling.py
