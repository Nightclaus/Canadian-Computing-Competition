import 'dart:io';
void main() {
  int maxInt = int.parse(stdin.readLineSync() ?? '');
  int radius = maxInt ~/ 2;
  List<String> array = [];
  for (int i = 0; i < maxInt; i++) {
    array.add(stdin.readLineSync() ?? '');
  }

  int result = 0;
  for (int i = 0; i < radius; i++) {
    if (array[i] == array[i+radius]) {
      result += 2;
    }
  }
  print(result);
}