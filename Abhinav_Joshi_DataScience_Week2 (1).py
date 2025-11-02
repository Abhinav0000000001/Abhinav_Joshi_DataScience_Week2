{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "7eb41dde-446d-471f-8a7d-6a084aec7e5f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "first number is a and second is b 12 2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "first number is 12 and second is 2\n",
      "Sum of number is 14\n",
      "Difference of number is 10\n",
      "Mulitplication of number is 24\n",
      "Division of number is 6.0\n",
      "Remainder of number iis 0\n",
      "Exponential of number is 144\n"
     ]
    }
   ],
   "source": [
    "# Take two integer value from User using Input function\n",
    "#Using Split method with input function for converting string to a list for unpacking\n",
    "#Convert Character to int using int and map function for mapping purpose\n",
    "a,b = map(int,(input('first number is a and second is b').split()))\n",
    "#Performing different airthmetic operations as given in the requirement\n",
    "Sum = a+b\n",
    "Difference = a-b\n",
    "Mult = a*b\n",
    "Div = a/b\n",
    "Mod = a%b\n",
    "exp = a**b\n",
    "print(f'first number is {a} and second is {b}')\n",
    "print(f'Sum of number is {Sum}')\n",
    "print(f'Difference of number is {Difference}')\n",
    "print(f'Mulitplication of number is {Mult}')\n",
    "print(f'Division of number is {Div}')\n",
    "print(f'Remainder of number iis {Mod}')\n",
    "print(f'Exponential of number is {exp}')\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "id": "5965e623-61db-4a6b-915e-ed710fcea53e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "19\n",
      "maximum number is 19\n",
      "minimumnumber is 1\n",
      "new list after appending [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 800]\n",
      "new list after removing a integer [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 800]\n",
      "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 800]\n",
      "[800, 19, 18, 17, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]\n"
     ]
    }
   ],
   "source": [
    "#Create a list with atleast 10 numbers\n",
    "numbers=[i for i in range (1,20)]\n",
    "#List Length\n",
    "print(len(numbers))\n",
    "#Max number\n",
    "print(f'maximum number is {max(numbers)}')\n",
    "#Min number\n",
    "print(f'minimumnumber is {min(numbers)}')\n",
    "#Adding one more element\n",
    "numbers.append(800)\n",
    "print(f'new list after appending {numbers}')\n",
    "#Removing element from list\n",
    "numbers.remove(16)\n",
    "print(f'new list after removing a integer {numbers}')\n",
    "#Soting List in ascending order\n",
    "numbers.sort()\n",
    "print(numbers)\n",
    "#Soting List in descending order\n",
    "numbers.sort(reverse=True)\n",
    "print(numbers)\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "id": "0f1b4ac7-261f-4d75-bb13-43543ee7e134",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "value of mean is 51.26315789473684\n",
      "value of median is 10.0\n",
      "value of standard deviation is 176.55827787097533\n"
     ]
    }
   ],
   "source": [
    "#Converting list to numpy array\n",
    "import numpy as np\n",
    "array=np.array(numbers)\n",
    "#Calculate Mean, Median, and Standard Deviation\n",
    "mean=np.mean(array)\n",
    "Median=np.median(array)\n",
    "std=np.std(array)\n",
    "print(f'value of mean is {mean}')\n",
    "print(f'value of median is {Median}')\n",
    "print(f'value of standard deviation is {std}')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "id": "fdfaabbc-1a68-4e14-9f43-ef81eafe3f41",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'numpy.ndarray'>\n"
     ]
    }
   ],
   "source": [
    "print(type(array))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "id": "13fafa79-ce08-4307-893d-580cbf9be0e4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Name\n",
      "Age\n",
      "Course\n",
      "Marks\n",
      "Name\n",
      "Age\n",
      "Course\n",
      "Marks\n",
      "Grade\n"
     ]
    }
   ],
   "source": [
    "#Dictionray name Student with key Name,Age,Course,Marks\n",
    "Student = {\"Name\":\"Arun\",\"Age\":25,\"Course\":\"DataScience\",\"Marks\":51}\n",
    "#key value using a loop\n",
    "for i in Student:\n",
    "    print(i)\n",
    "#add new Element Grade\n",
    "Student[\"Grade\"]=\"B\"\n",
    "#Cross check whether Grade got added or not\n",
    "for i in Student:\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "id": "a9644c54-e47c-499c-8d37-1f6f7c84caa5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'AI', 'Data Science', 'Python'}\n"
     ]
    }
   ],
   "source": [
    "#Using Set to fetch unique values\n",
    "course_list = [\"Python\", \"Data Science\", \"AI\", \"Python\"]\n",
    "unique_courses = set(course_list)\n",
    "print(unique_courses)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "id": "ca80ba2e-20f5-4c98-abc7-e6090127e39e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Union: {'Machine Learning', 'Data Science', 'AI', 'Python'}\n",
      "Intersection: {'AI', 'Python'}\n",
      "Difference (set1 - set2): {'Data Science'}\n",
      "Difference (set2 - set1): {'Machine Learning'}\n"
     ]
    }
   ],
   "source": [
    "#Perform set operations — union, intersection, and difference — between two sets of sample data.\n",
    "set1 = {\"Python\", \"Data Science\", \"AI\"}\n",
    "set2 = {\"AI\", \"Machine Learning\", \"Python\"}\n",
    "#Union — Combines all unique elements from both sets\n",
    "print(\"Union:\", set1.union(set2))\n",
    "#Intersection — Elements common to both sets\n",
    "print(\"Intersection:\", set1.intersection(set2))\n",
    "#Difference — Elements present in one set but not in the other\n",
    "print(\"Difference (set1 - set2):\", set1.difference(set2))\n",
    "print(\"Difference (set2 - set1):\", set2.difference(set1))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 129,
   "id": "118e791d-2112-4253-93a8-c3cb05da23cc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Student data written successfully to 'student_data.txt'!\n"
     ]
    }
   ],
   "source": [
    "#Create a text file named student_data.txt.\n",
    "#Write the following information into the file (name, course, and marks of at least 5 students).\n",
    "\n",
    "with open(\"student_data.txt\", \"w\") as f:\n",
    "    f.write(\"Name\\t\\tCourse\\t\\tMarks\\n\")\n",
    "    f.write(\"----------------------------------\\n\")\n",
    "    f.write(\"Arun\\t\\tData Science\\t51\\n\")\n",
    "    f.write(\"Neha\\t\\tPython\\t\\t\\t78\\n\")\n",
    "    f.write(\"Ravi\\t\\tAI\\t\\t\\t85\\n\")\n",
    "    f.write(\"Simran\\t\\tMachine Learning\\t92\\n\")\n",
    "    f.write(\"Aman\\t\\tStatistics\\t\\t67\\n\")\n",
    "print(\"Student data written successfully to 'student_data.txt'!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "efddf1f2-8895-426b-a29a-1cc1aa5a2737",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9707e014-947b-4812-9ba3-0a5b5d5a254a",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
