export const orderColumns = [
    { field: "id", headerName: "ID", width: 70 },
    {
        field: "category",
        headerName: "Category",
        width: 160,
        renderCell: (params) => {
          return (
            <div className={`cellWithCategory ${params.row.category}`}>
              {params.row.category}
            </div>
          );
        },
      },
    
      {
        field: "Name",
        headerName: "name",
        width: 200,
      },
    {
      field: "agency",
      headerName: "Agency",
      width: 200,
    },
  
    {
      field: "company",
      headerName: "Company",
      width: 200,
    },
    {
        field: "deadline",
        headerName: "Deadline",
        width: 200,
      },
  ];
  
  //temporary data
  export const orderRows = [
    {
      id: 1,
      category: "Hidraulica",
      contact: "Alcides 1199999999-9999",
      agency: "Imobiliaria Sampa",
      company: "Reparos S.A",
      deadline: "02-02-2022",
    }
  ];
  