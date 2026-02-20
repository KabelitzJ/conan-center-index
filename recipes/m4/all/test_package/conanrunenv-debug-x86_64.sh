script_folder="/home/jxk10011/Documents/conan-center-index/recipes/m4/all/test_package"
echo "echo Restoring environment" > "$script_folder/deactivate_conanrunenv-debug-x86_64.sh"
for v in M4 PATH
do
   is_defined="true"
   value=$(printenv $v) || is_defined="" || true
   if [ -n "$value" ] || [ -n "$is_defined" ]
   then
       echo export "$v='$value'" >> "$script_folder/deactivate_conanrunenv-debug-x86_64.sh"
   else
       echo unset $v >> "$script_folder/deactivate_conanrunenv-debug-x86_64.sh"
   fi
done

export M4="/home/jxk10011/.conan2/p/b/m4c27916a16378a/p/bin/m4"
export PATH="/home/jxk10011/.conan2/p/b/m4c27916a16378a/p/bin:$PATH"