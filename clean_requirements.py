{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "535a579a-0a37-42bf-bcdc-e72b3213c771",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "requirements.txt limpio creado con éxito.\n"
     ]
    }
   ],
   "source": [
    "import re\n",
    "\n",
    "# Leer el contenido del archivo requirements.txt\n",
    "with open('requirements.txt', 'r') as f:\n",
    "    lines = f.readlines()\n",
    "\n",
    "# Filtrar líneas que contienen rutas locales (file://) y mantener solo las líneas con el formato correcto\n",
    "clean_lines = [re.sub(r'\\s*@.*', '', line) for line in lines]\n",
    "\n",
    "# Escribir el nuevo archivo requirements.txt limpio\n",
    "with open('requirements.txt', 'w') as f:\n",
    "    f.writelines(clean_lines)\n",
    "\n",
    "print(\"requirements.txt limpio creado con éxito.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2571a8cc-f6d7-4a3c-8443-9ed276450bcb",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "“aprendizaje”",
   "language": "python",
   "name": "aprendizaje"
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
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
