import discord 
from typing import List, Union

class ComponentBuilder(discord.ui.View):
    """
    Builder para criar um `discord.ui.View` com componentes interativos como botões ou menus.

    Essa classe permite adicionar um único componente ou uma lista de componentes (exceto modais e text inputs, que são tratados separadamente).

    Args:
        component (Union[List[discord.Component], discord.Component]):
            Um ou mais componentes (como `discord.ui.Button`, `discord.ui.Select`, etc.) a serem adicionados à view.
        persistent (bool, optional):
            Se `True`, a view não expira (timeout = None). Caso contrário, expira em 180 segundos. Padrão é `False`.

    Raises:
        TypeError: Se nenhum componente for passado.
        TypeError: Se um componente inválido for incluído (ex: `discord.ui.Modal` ou `discord.ui.TextInput`).

    Exemplo:
        button = discord.ui.Button(label="Clique aqui", style=discord.ButtonStyle.primary)
        view = ComponentBuilder(component=button)

        await interaction.response.send_message("Clique no botão!", view=view)
    """
    
    def __init__(
        self, 
        components: Union[List[discord.ui.Item], discord.ui.Item], 
        persistent: bool=None
    ) -> None:
        super().__init__(
            timeout=None if persistent else 180
        )
        
        if isinstance(components, list):
            for component in components:
                self.add_item(component)
        
        elif isinstance(components, discord.ui.Item):
            self.add_item(components)