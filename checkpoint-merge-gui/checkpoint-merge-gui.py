import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.ttk import Progressbar
import torch
from safetensors.torch import load_file, save_file  # Para lidar com arquivos .safetensors
import time  # Para simular progresso (apenas para demonstração)

def select_file(entry):
    filepath = filedialog.askopenfilename(
        filetypes=[("Stable Diffusion Checkpoints", "*.ckpt *.safetensors")]
    )
    if filepath:
        entry.delete(0, tk.END)
        entry.insert(0, filepath)

def save_merged_file(entry):
    filepath = filedialog.asksaveasfilename(
        defaultextension=".ckpt",
        filetypes=[("Stable Diffusion Checkpoints", "*.ckpt *.safetensors")]
    )
    if filepath:
        entry.delete(0, tk.END)
        entry.insert(0, filepath)

def load_checkpoint(file_path):
    """Carrega o checkpoint de acordo com o formato do arquivo."""
    log_message(f"Carregando arquivo: {file_path}")
    if file_path.endswith(".safetensors"):
        return load_file(file_path)  # Carregar arquivo .safetensors
    elif file_path.endswith(".ckpt"):
        return torch.load(file_path, map_location="cpu", weights_only=True)
    else:
        raise ValueError("Formato de arquivo não suportado. Use .ckpt ou .safetensors.")

def save_checkpoint(data, file_path):
    """Salva o checkpoint de acordo com o formato do arquivo."""
    log_message(f"Salvando arquivo mesclado em: {file_path}")
    if file_path.endswith(".safetensors"):
        save_file(data, file_path)  # Salvar como .safetensors
    elif file_path.endswith(".ckpt"):
        torch.save(data, file_path)
    else:
        raise ValueError("Formato de arquivo não suportado. Use .ckpt ou .safetensors.")

def log_message(message):
    """Adiciona uma mensagem ao log."""
    log.insert(tk.END, message)
    log.see(tk.END)  # Rola automaticamente para a última mensagem

def merge_checkpoints():
    ckpt1_path = entry_ckpt1.get()
    ckpt2_path = entry_ckpt2.get()
    save_path = entry_save.get()
    
    if not ckpt1_path or not ckpt2_path or not save_path:
        messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
        return

    try:
        # Resetar barra de progresso e log
        progress["value"] = 0
        log.delete(1.0, tk.END)

        # Carregar checkpoints
        log_message("Iniciando mesclagem dos checkpoints...")
        ckpt1 = load_checkpoint(ckpt1_path)
        progress["value"] = 33  # Atualiza progresso
        root.update_idletasks()

        ckpt2 = load_checkpoint(ckpt2_path)
        progress["value"] = 66  # Atualiza progresso
        root.update_idletasks()
        
        # Mesclar checkpoints
        log_message("Mesclando os checkpoints...")
        merged_ckpt = {}
        for key in ckpt1.keys():
            if key in ckpt2:
                merged_ckpt[key] = 0.5 * (ckpt1[key] + ckpt2[key])
            else:
                merged_ckpt[key] = ckpt1[key]

        for key in ckpt2.keys():
            if key not in ckpt1:
                merged_ckpt[key] = ckpt2[key]

        progress["value"] = 90  # Atualiza progresso
        root.update_idletasks()

        # Salvar checkpoint mesclado
        save_checkpoint(merged_ckpt, save_path)
        progress["value"] = 100  # Concluído
        log_message("Mesclagem concluída com sucesso!")
        messagebox.showinfo("Sucesso", f"Checkpoint mesclado salvo como: {save_path}")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao mesclar checkpoints:\n{str(e)}")
        log_message(f"Erro: {str(e)}")

# Criação da interface gráfica
root = tk.Tk()
root.title("Stable Diffusion Checkpoint Merge")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

# Caminho do Checkpoint 1
tk.Label(frame, text="Checkpoint 1:").grid(row=0, column=0, sticky="w")
entry_ckpt1 = tk.Entry(frame, width=40)
entry_ckpt1.grid(row=0, column=1, padx=5, pady=5)
btn_ckpt1 = tk.Button(frame, text="Selecionar", command=lambda: select_file(entry_ckpt1))
btn_ckpt1.grid(row=0, column=2)

# Caminho do Checkpoint 2
tk.Label(frame, text="Checkpoint 2:").grid(row=1, column=0, sticky="w")
entry_ckpt2 = tk.Entry(frame, width=40)
entry_ckpt2.grid(row=1, column=1, padx=5, pady=5)
btn_ckpt2 = tk.Button(frame, text="Selecionar", command=lambda: select_file(entry_ckpt2))
btn_ckpt2.grid(row=1, column=2)

# Caminho do arquivo mesclado
tk.Label(frame, text="Salvar como:").grid(row=2, column=0, sticky="w")
entry_save = tk.Entry(frame, width=40)
entry_save.grid(row=2, column=1, padx=5, pady=5)
btn_save = tk.Button(frame, text="Selecionar", command=lambda: save_merged_file(entry_save))
btn_save.grid(row=2, column=2)

# Barra de progresso
progress = Progressbar(frame, orient="horizontal", length=300, mode="determinate")
progress.grid(row=3, column=0, columnspan=3, pady=10)

# Área de log
log_label = tk.Label(frame, text="Log:")
log_label.grid(row=4, column=0, sticky="w")
log = tk.Text(frame, height=10, width=50, state="normal", wrap="word")
log.grid(row=5, column=0, columnspan=3, pady=5)

# Botão de mesclar
btn_merge = tk.Button(frame, text="Mesclar", command=merge_checkpoints, bg="green", fg="white")
btn_merge.grid(row=6, column=0, columnspan=3, pady=10)

# Rodapé com crédito
footer = tk.Label(root, text="Criado por Drifer97", fg="gray", font=("Arial", 10))
footer.pack(side="bottom", pady=5)

root.mainloop()
