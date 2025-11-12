import fitz  # PyMuPDF
import argparse
import os

def resize_pdf_to_a4(input_path, output_path):
    """
    Redimensionne un PDF pour l'adapter au format A4 tout en conservant le ratio.
    """
    # Dimensions du format A4 en points (72 dpi)
    a4_width = 595
    a4_height = 842

    try:
        # Ouvrir le document PDF source
        doc = fitz.open(input_path)
    except Exception as e:
        print(f"Erreur : Impossible d'ouvrir le fichier {input_path}. Vérifiez que c'est un PDF valide.")
        print(f"Détails : {e}")
        return

    # Créer un nouveau document PDF pour la sortie
    new_doc = fitz.open()

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        rect = page.rect
        width, height = rect.width, rect.height

        # Calculer le ratio de redimensionnement pour s'adapter à l'A4
        w_ratio = a4_width / width
        h_ratio = a4_height / height
        scaling_factor = min(w_ratio, h_ratio)

        # Les nouvelles dimensions de la page source
        new_width = width * scaling_factor
        new_height = height * scaling_factor

        # Créer une nouvelle page A4
        new_page = new_doc.new_page(width=a4_width, height=a4_height)

        # Calculer la position pour centrer le contenu
        x_pos = (a4_width - new_width) / 2
        y_pos = (a4_height - new_height) / 2

        # Définir le rectangle où le contenu sera inséré
        target_rect = fitz.Rect(x_pos, y_pos, x_pos + new_width, y_pos + new_height)

        # Insérer le contenu de l'ancienne page dans la nouvelle
        new_page.show_pdf_page(target_rect, doc, page.number)

    try:
        # Sauvegarder le nouveau document
        new_doc.save(output_path, garbage=4, deflate=True, clean=True)
        print(f"PDF redimensionné et sauvegardé avec succès sous : {output_path}")
    except Exception as e:
        print(f"Erreur lors de la sauvegarde du fichier {output_path}.")
        print(f"Détails : {e}")
    finally:
        doc.close()
        new_doc.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Redimensionne un fichier PDF au format A4 tout en conservant le ratio d'aspect.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        "input_file",
        help="Chemin vers le fichier PDF d'entrée."
    )
    parser.add_argument(
        "-o", "--output",
        dest="output_file",
        help="Chemin vers le fichier PDF de sortie.\\nSi non spécifié, le nom sera 'input_file_resized.pdf'.",
        default=None
    )

    args = parser.parse_args()

    # Déterminer le nom du fichier de sortie
    if args.output_file:
        output_filename = args.output_file
    else:
        base, ext = os.path.splitext(args.input_file)
        output_filename = f"{base}_resized{ext}"

    # Vérifier si le fichier d'entrée existe
    if not os.path.exists(args.input_file):
        print(f"Erreur : Le fichier d'entrée '{args.input_file}' n'a pas été trouvé.")
    else:
        resize_pdf_to_a4(args.input_file, output_filename)
